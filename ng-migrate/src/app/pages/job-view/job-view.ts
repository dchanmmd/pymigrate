import { httpResource } from "@angular/common/http";
import { Component, computed } from "@angular/core";
import { JobSummary } from "@common/interface/job-summary.interface";
import { ListResponse } from "@common/interface/list-response.interface";
import { JobCard } from "@components/job-card/job-card";
import { Header } from "@components/header/header";
import { environment } from "@environments/environment";
import { Spinner } from "@app/components/spinner/spinner";

@Component({
    selector: "app-job-view",
    imports: [Header, JobCard, Spinner],
    templateUrl: "./job-view.html"
})
export class JobView {
    public response = httpResource<ListResponse<JobSummary>>(() => new URL("/api/v1/transfers", environment.apiUrl).toString());
    jobs = computed(() => this.response.value()?.data);
}
