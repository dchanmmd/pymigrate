import { Component, input, InputSignal } from "@angular/core";

type TooltipPosition = "top" | "bottom" | "left" | "right";

@Component({
    selector: "app-tooltip",
    imports: [],
    templateUrl: "./tooltip.html",
    styleUrl: "./tooltip.css",
})
export class Tooltip {
    public tip: InputSignal<string> = input.required<string>();
    public position: InputSignal<TooltipPosition> = input.required<TooltipPosition>();
}
