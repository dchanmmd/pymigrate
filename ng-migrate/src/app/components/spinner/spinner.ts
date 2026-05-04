import { Component, input, InputSignal } from "@angular/core";

@Component({
    selector: "app-spinner",
    imports: [],
    templateUrl: "./spinner.html"
})
export class Spinner {
    public size: InputSignal<number> = input(36);
    public fill: InputSignal<string> = input("fill-indigo-500");
}
