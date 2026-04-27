import { Component, computed, input, InputSignal, Signal } from "@angular/core";
import { RouterModule } from "@angular/router";

@Component({
    selector: "app-branch-card",
    standalone: true,
    imports: [RouterModule],
    templateUrl: "./branch-card.html"
})
export class BranchCard {
    id: InputSignal<number> = input.required<number>();
    name: InputSignal<string> = input.required<string>();

    title: Signal<string> = computed(() => this.name()
        .split(" ")
        .filter(Boolean)
        .map(w => w.at(0)?.toUpperCase() + w.slice(1).toLowerCase())
        .join(" ")
    );
}
