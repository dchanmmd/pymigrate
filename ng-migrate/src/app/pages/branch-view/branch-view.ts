import { Component, computed  } from "@angular/core";
import { Header } from "@components/header/header";
import { Branch } from "@common/interface/branch.interface";
import { BranchCard } from "@components/branch-card/branch-card";
import { httpResource } from "@angular/common/http";
import { ListResponse } from "@app/common/interface/list-response.interface";
import { environment } from "@environments/environment";
import { Spinner } from "@app/components/spinner/spinner";

@Component({
    selector: "app-branch-view",
    imports: [Header, BranchCard, Spinner],
    templateUrl: "./branch-view.html"
})
export class BranchView {
    public response = httpResource<ListResponse<Branch>>(() => new URL(`/api/v1/branches`, environment.apiUrl).toString());
    public branches = computed(() => this.response.value()?.data);
}
