import { httpResource } from "@angular/common/http";
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
import { debounceTime, distinctUntilChanged } from "rxjs";

@Component({
    selector: "app-inventory-view",
    imports: [Header, Dialog, Spinner, Tooltip],
    templateUrl: "./inventory-view.html"
})
export class InventoryView {
    public activatedRoute = inject(ActivatedRoute);
    public reloading: WritableSignal<boolean> = signal(false);
    public branchId: string = this.activatedRoute.snapshot.paramMap.get("id") ?? "";
    public dialog: Signal<Dialog> = viewChild.required(Dialog);
    public query: WritableSignal<string> = signal("");
    public debouncedQuery = toSignal(
        toObservable(this.query).pipe(
            debounceTime(500),
            distinctUntilChanged()
        ),
        { initialValue: "" }
    );

    public response = httpResource<ItemResponse<InventoryItem>>(() => {
        const url = new URL(`/api/v1/${this.branchId}`, environment.apiUrl);
        url.searchParams.set("query", this.debouncedQuery().trim());
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
}