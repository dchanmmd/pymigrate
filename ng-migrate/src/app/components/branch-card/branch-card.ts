import { Component, computed, input, InputSignal, Signal } from "@angular/core";
import { RouterModule } from "@angular/router";
import { toMMDTitle } from "@app/common/lib/functions";

@Component({
    selector: "app-branch-card",
    standalone: true,
    imports: [RouterModule],
    templateUrl: "./branch-card.html"
})
export class BranchCard {
    id: InputSignal<number> = input.required<number>();
    name: InputSignal<string> = input.required<string>();

    title: Signal<string> = computed(() => toMMDTitle(this.name()));
}
