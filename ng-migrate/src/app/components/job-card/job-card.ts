import { Component, computed, input, InputSignal } from "@angular/core";
import { ItemResult } from "@app/common/enum/item-result.enum";
import { JobSummary } from "@app/common/interface/job-summary.interface";
import { JobStatus } from "@common/enum/job-status.enum";

@Component({
    selector: "app-job-card",
    imports: [],
    templateUrl: "./job-card.html"
})
export class JobCard {
    protected readonly JobStatus = JobStatus;
    public format = new Intl.DateTimeFormat("es-419", {
        dateStyle: "long",
        timeStyle: "short",
    });
    public job: InputSignal<JobSummary> = input.required();
    public count = computed(() => this.job().items.length);
    public pushedAt = computed(() => this.format.format(new Date(this.job().pushed_at)));

    public success = computed(() => this.job().recount[ItemResult.Success]);
    public failure = computed(() => this.job().recount[ItemResult.Failure]);
    public pending = computed(() => this.job().recount[ItemResult.Pending]);
}
