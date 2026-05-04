import { Component, input, InputSignal } from "@angular/core";
import { RouterModule } from "@angular/router";
import { Branch } from "@app/common/interface/branch.interface";
import { toMMDTitle } from "@app/common/lib/functions";

@Component({
    selector: "app-branch-card",
    standalone: true,
    imports: [RouterModule],
    templateUrl: "./branch-card.html"
})
export class BranchCard {
    branch: InputSignal<Branch> = input.required<Branch>();

    public toMMDTitle(text: string): string {
        return toMMDTitle(text);
    }
}
