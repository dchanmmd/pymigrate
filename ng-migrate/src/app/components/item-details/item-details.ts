import { Component, computed, input, InputSignal, output, OutputEmitterRef } from "@angular/core";
import { InventoryItem } from "@common/interface/inventory-item.interface";
import { toMoney } from "@common/lib/functions";

@Component({
    selector: "app-item-details",
    imports: [],
    templateUrl: "./item-details.html"
})
export class ItemDetails {
    public item: InputSignal<InventoryItem> = input.required();
    public selection: InputSignal<Set<InventoryItem>> = input.required<Set<InventoryItem>>();
    public selected: OutputEmitterRef<InventoryItem> = output<InventoryItem>();
    public checked = computed(() =>
        Array.from(this.selection()).some(i => i.barcode === this.item().barcode)
    );

    public toMoney(money: number): string {
        return toMoney(money);
    }
}
