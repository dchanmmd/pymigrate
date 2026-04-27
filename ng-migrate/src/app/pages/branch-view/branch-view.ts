import { Component } from "@angular/core";
import { Header } from "../../components/header/header";
import { httpResource } from "@angular/common/http";
import { Branch } from "../../common/interface/branch.interface";
import { environment } from "../../../environments/environment";
import { BranchCard } from "../../components/branch-card/branch-card";

@Component({
    selector: "app-branch-view",
    imports: [Header, BranchCard],
    templateUrl: "./branch-view.html"
})
export class BranchView {
    branches = httpResource<Array<Branch>>(
        () => new URL("/api/v1/branches", environment.apiUrl).toString(),
        { defaultValue: [] }
    );
}
