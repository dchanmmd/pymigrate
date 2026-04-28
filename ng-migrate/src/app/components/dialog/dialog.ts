import { Component, input, InputSignal, signal, WritableSignal } from "@angular/core";

@Component({
    selector: "app-dialog",
    imports: [],
    templateUrl: "./dialog.html"
})
export class Dialog {
    public open: WritableSignal<boolean> = signal(false);
    public modal: InputSignal<boolean> = input(false);

    public closeNonModal() {
        if (!this.modal()) this.open.set(false);
    }

    public show() {
        this.open.set(true);
    }

    public close() {
        this.open.set(false);
    }
}
