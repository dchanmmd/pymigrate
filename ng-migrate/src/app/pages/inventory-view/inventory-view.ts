import { Component, computed, inject, signal, Signal, viewChild, WritableSignal } from "@angular/core";
import { Header } from "@components/header/header";
import { ActivatedRoute } from "@angular/router";
import { toObservable, toSignal } from "@angular/core/rxjs-interop";
import { BranchService } from "../branch-view/branch.service";
import { combineLatest, debounceTime, distinctUntilChanged, filter, map, startWith, Subject, switchMap, tap } from "rxjs";
import { Branch } from "@app/common/interface/branch.interface";
import { InventoryItem } from "@app/common/interface/inventory-item.interface";
import { InventoryService } from "./inventory.service";
import { toMMDTitle } from "@app/common/lib/functions";
import { FormsModule } from "@angular/forms";
import { Badge } from "@app/components/badge/badge";
import { Dialog } from "@app/components/dialog/dialog";

@Component({
    selector: "app-inventory-view",
    imports: [Header, FormsModule, Badge, Dialog],
    templateUrl: "./inventory-view.html"
})
export class InventoryView {
    private readonly branchService = inject(BranchService);
    private readonly inventoryService = inject(InventoryService);

    private readonly activatedRoute = inject(ActivatedRoute);

    private readonly pageSize: number = 10;

    public page: WritableSignal<number> = signal(1);
    public count: WritableSignal<number> = signal(1);
    public query: WritableSignal<string> = signal("");

    public dialog = viewChild.required(Dialog);
    public dialogMode: WritableSignal<"detail" | "confirm"> = signal("detail");
    public selectedItem: WritableSignal<InventoryItem | null> = signal(null);

    public page$ = toObservable(this.page);
    public query$ = toObservable(this.query).pipe(debounceTime(300), distinctUntilChanged(), tap(() => this.page.set(1)));
    public refresh$ = new Subject<void>();

    public selectedBarcodes: WritableSignal<Set<string>> = signal(new Set());

    public toMoney(num: number): string {
        const fixed = num.toFixed(2);
        const [integer, decimal] = fixed.split(".");
        const fragments = [];

        for (let i = integer.length; i > 0; i -= 3) {
            fragments.unshift(integer.slice(Math.max(0, i - 3), i));
        }

        return `${fragments.join(",")}.${decimal}`;
    }

    private readonly branchId = this.activatedRoute.paramMap.pipe(
        map(params => params.get("id") ?? ""),
        filter(Boolean)
    );

    public readonly branch: Signal<Branch | undefined> = toSignal(
        this.branchId.pipe(
            switchMap(id => this.branchService.fetchBranch(id)),
            map(r => ({ id: r.data.id, name: toMMDTitle(r.data.name) }))
        )
    );

    public readonly inventory: Signal<Array<InventoryItem> | undefined> = toSignal(
        this.branchId.pipe(
            switchMap(branchId =>
                combineLatest([this.query$, this.page$, this.refresh$.pipe(startWith(null))]).pipe(
                    switchMap(([query, page]) =>
                        this.inventoryService.fetchInventory(branchId, page, query)
                    ),
                    tap(r => this.count.set(r.metadata?.["count"] || 0)),
                    map(r => r.data)
                )
            )
        )
    );

    public clearSearchBar() {
        this.query.set("");
        this.page.set(1);
    }

    public nextPage() {
        this.page.update(p => Math.min(Math.ceil(this.count() / this.pageSize), p + 1));
    }

    public prevPage() {
        this.page.update(p => Math.max(1, p - 1));
    }

    public refresh() {
        this.refresh$.next();
    }

    public openDetail(item: InventoryItem) {
        this.selectedItem.set(item);
        this.dialogMode.set("detail");
        this.dialog().show();
    }

    public openConfirm() {
        if (!this.selectedCount()) return;
        this.selectedItem.set(null);
        this.dialogMode.set("confirm");
        this.dialog().show();
    }

    public isSelected(barcode: string): boolean {
        return this.selectedBarcodes().has(barcode);
    }

    public toggleItem(barcode: string) {
        this.selectedBarcodes.update(set => {
            const next = new Set(set);
            next.has(barcode) ? next.delete(barcode) : next.add(barcode);
            return next;
        });
    }


    public toggleAndClose(barcode: string) {
        this.toggleItem(barcode);
        this.dialog().close();
    }

    public isAllSelected(): boolean {
        const items = this.inventory();
        return !!items?.length && items.every(i => this.selectedBarcodes().has(i.barcode));
    }

    public toggleAll() {
        const items = this.inventory() ?? [];
        if (this.isAllSelected()) {
            this.selectedBarcodes.update(set => {
                const next = new Set(set);
                items.forEach(i => next.delete(i.barcode));
                return next;
            });
        } else {
            this.selectedBarcodes.update(set => {
                const next = new Set(set);
                items.forEach(i => next.add(i.barcode));
                return next;
            });
        }
    }

    public onFormSubmit(event: SubmitEvent) {
        event.preventDefault();
        if (!this.selectedCount()) return;
        this.inventoryService.sendSelection(Array.from(this.selectedBarcodes())).subscribe({
            next: () => {

            },
            complete: () => {
                this.selectedBarcodes.update(() => new Set());
                this.dialog().close();
            }
        });
    }

    public readonly totalPages = computed(() => Math.ceil(this.count() / this.pageSize));
    public readonly hasNextPage = computed(() => this.page() < this.totalPages());
    public readonly hasPrevPage = computed(() => this.page() > 1);
    public readonly selectedCount = computed(() => this.selectedBarcodes().size);
}