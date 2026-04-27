import { Component, input, InputSignal, output, OutputEmitterRef } from "@angular/core";

@Component({
    selector: "app-alert",
    standalone: true,
    templateUrl: "./alert.html",
})
export class Alert {
    alertText: InputSignal<string> = input.required<string>();
    close: OutputEmitterRef<void> = output<void>();
}
