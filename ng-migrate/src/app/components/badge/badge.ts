import { Component, input, InputSignal } from "@angular/core";

@Component({
    selector: "app-badge",
    imports: [],
    templateUrl: "./badge.html",
    styleUrl: "./badge.css"
})
export class Badge {
    public text: InputSignal<string> = input("");
}
