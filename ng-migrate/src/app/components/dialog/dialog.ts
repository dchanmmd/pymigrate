import { Component, signal, WritableSignal } from "@angular/core"; 

@Component({ 
    selector: "app-dialog", 
    imports: [], 
    templateUrl: "./dialog.html",
    styleUrl: "./dialog.css"
}) 
export class Dialog { 
    public open: WritableSignal<boolean> = signal(false); 
    public displayed: WritableSignal<boolean> = signal(false); 
    
    public show(): void { 
        this.open.set(true);
        requestAnimationFrame(() => this.displayed.set(true));
    } 

    public hide(): void { 
        this.displayed.set(false); 
        setTimeout(() => { 
            this.open.set(false); 
        }, 300); 
    } 
}