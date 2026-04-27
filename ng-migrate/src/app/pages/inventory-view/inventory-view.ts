import { Component, OnInit } from "@angular/core";
import { ActivatedRoute } from "@angular/router";

@Component({
    selector: "app-inventory-view",
    imports: [],
    templateUrl: "./inventory-view.html"
})
export class InventoryView implements OnInit {
    constructor(private readonly route: ActivatedRoute) { }

    id: string | null = null;

    ngOnInit(): void {
        this.route.paramMap.subscribe(params => this.id = params.get("id"));
    }
}
