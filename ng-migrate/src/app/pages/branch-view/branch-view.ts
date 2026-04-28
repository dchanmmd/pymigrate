import { Component, inject, Signal,  } from "@angular/core";
import { Header } from "@components/header/header";
import { Branch } from "@common/interface/branch.interface";
import { BranchCard } from "@components/branch-card/branch-card";
import { BranchService } from "./branch.service";
import { toSignal } from "@angular/core/rxjs-interop";
import { map, tap } from "rxjs";

@Component({
    selector: "app-branch-view",
    imports: [Header, BranchCard],
    templateUrl: "./branch-view.html"
})
export class BranchView {
    private readonly branchService: BranchService = inject(BranchService);
    public branches: Signal<Array<Branch>> = toSignal(
        this.branchService.fetchBranchList().pipe(tap(response => console.log(response)), map(response => response.data)),
        { initialValue: [] }
    );
}
