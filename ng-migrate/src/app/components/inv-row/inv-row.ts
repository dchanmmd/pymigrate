import { Component, computed, input, InputSignal, output, OutputEmitterRef } from "@angular/core";
import { InventoryItem } from "@common/interface/inventory-item.interface";
import { toMoney } from "@common/lib/functions";
import { Tooltip } from "../tooltip/tooltip";

@Component({
    selector: "tr[inv-row]",
    imports: [Tooltip],
    templateUrl: "./inv-row.html"
})
export class InvRow {
    public item: InputSignal<InventoryItem> = input.required();
    public selection: InputSignal<Set<InventoryItem>> = input.required<Set<InventoryItem>>();
    public selected: OutputEmitterRef<InventoryItem> = output<InventoryItem>();
    public detail: OutputEmitterRef<void> = output<void>();
    public checked = computed(() =>
        Array.from(this.selection()).some(i => i.barcode === this.item().barcode)
    );

    public toMoney(money: number): string {
        return toMoney(money);
    }
}
