import { Component } from "@angular/core";
import { RouterModule } from "@angular/router";
import { Tooltip } from "../tooltip/tooltip";

@Component({
    selector: "app-header",
    standalone: true,
    imports: [RouterModule, Tooltip],
    templateUrl: "./header.html"
})
export class Header {}
