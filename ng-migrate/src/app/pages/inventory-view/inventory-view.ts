import { httpResource, HttpErrorResponse } from "@angular/common/http";
import { Component, computed, inject, signal, Signal, viewChild, WritableSignal } from "@angular/core";
import { ActivatedRoute } from "@angular/router";
import { Spinner } from "@app/components/spinner/spinner";
import { InventoryItem } from "@common/interface/inventory-item.interface";
import { ItemResponse } from "@common/interface/item-response.interface";
import { Dialog } from "@components/dialog/dialog";
import { Header } from "@components/header/header";
import { environment } from "@environments/environment";
import { Tooltip } from "@components/tooltip/tooltip";
import { toObservable, toSignal } from "@angular/core/rxjs-interop";
import { debounceTime, distinctUntilChanged, map } from "rxjs";
import { Branch } from "@app/common/interface/branch.interface";
import { InvRow } from "@app/components/inv-row/inv-row";
import { ItemDetails } from "@app/components/item-details/item-details";


type DialogType = "details" | "confirmation";

@Component({
    selector: "app-inventory-view",
    imports: [Header, Dialog, Spinner, Tooltip, InvRow, ItemDetails],
    templateUrl: "./inventory-view.html"
})
export class InventoryView {
    public activatedRoute = inject(ActivatedRoute);
    public reloading: WritableSignal<boolean> = signal(false);
    public branchId: string = this.activatedRoute.snapshot.paramMap.get("id") ?? "";
    public dialog: Signal<Dialog> = viewChild.required(Dialog);
    public dialogType: WritableSignal<DialogType> = signal("details");
    public selection: WritableSignal<Set<InventoryItem>> = signal(new Set());
    public query: WritableSignal<string> = signal("");
    public debouncedQuery = toSignal(
        toObservable(this.query).pipe(
            debounceTime(500),
            distinctUntilChanged(),
            map(q => q.trim())
        ),
        { initialValue: "" }
    );

    public branchResponse = httpResource<ItemResponse<Branch>>(() => {
        const url = new URL(`/api/v1/branches/${this.branchId}`, environment.apiUrl);
        return url.toString();
    });

    public branch: Signal<Branch | undefined> = computed(() => this.branchResponse.value()?.data);

    public response = httpResource<ItemResponse<InventoryItem>>(() => {
        if (!this.debouncedQuery()) return undefined;
        const url = new URL(`/api/v1/inventory/${this.branchId}`, environment.apiUrl);
        url.searchParams.set("query", this.debouncedQuery());
        return url.toString();
    });

    public item: Signal<InventoryItem | undefined> = computed(() => this.response.value()?.data);

    public reload() {
        this.reloading.set(true);
        this.response.reload();
        setTimeout(() => {
            this.reloading.set(false);
        }, 500);
    }

    public setQuery(event: Event): void {
        this.query.set((event.currentTarget as HTMLInputElement).value);
    }

    public clearQuery(): void {
        this.query.set("");
    }

    public showItemDetails(): void {
        this.dialogType.set("details");
        this.dialog().show();
    }

    public showConfirmationDialog(): void {
        this.dialogType.set("confirmation");
        this.dialog().show();
    }

    public toggleRow(row: InventoryItem): void {
        this.selection.update(s => {
            const next = new Set(s);
            const existing = [...next].find(i => i.barcode === row.barcode);

            existing ? next.delete(existing) : next.add(row);

            return next;
        });
    }

    public toggleAndClose(row: InventoryItem): void {
        this.toggleRow(row);
        this.dialog().hide();
    }

    public toMMDTitle = (text: string) => {
        const words = text.split(" ").filter(Boolean).map(w => w.trim().toLowerCase());
        const result = [];

        for (let word of words) {
            if (word === "masmedan") {
                result.push("Más Me Dan");
            } else if (["cc", "mmd", "si", "mmdsi", "cf"].includes(word)) {
                result.push(word.toUpperCase());
            } else {
                result.push(word.at(0)?.toUpperCase() + word.slice(1).toLowerCase());
            }
        }

        return result.join(" ");
    };

}