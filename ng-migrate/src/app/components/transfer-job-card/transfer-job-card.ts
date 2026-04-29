import { Component, computed, input, InputSignal, Signal } from "@angular/core";
import { ItemResult } from "@app/common/enum/item-result.enum";
import { JobSummary } from "@app/common/interface/job-summary.interface";

@Component({
    selector: "app-transfer-job-card",
    imports: [],
    templateUrl: "./transfer-job-card.html"
})
export class TransferJobCard {
    dateFormat = new Intl.DateTimeFormat('es-419', {
        dateStyle: 'long',
        timeStyle: 'short',
        timeZone: 'America/Bogota'
    });

    job: InputSignal<JobSummary> = input.required();

    status: Signal<string> = computed(() => this.job().status);
    total: Signal<number> = computed(() => this.job().items.length);
    success: Signal<number> = computed(() => this.job().recount[ItemResult.Success]);
    failure: Signal<number> = computed(() => this.job().recount[ItemResult.Failure]);
    pending: Signal<number> = computed(() => this.job().recount[ItemResult.Pending]);
    date: Signal<string> = computed(() => this.dateFormat.format(new Date(this.job().pushed_at)));

    public title(text: string): string {
        return text.split(" ").filter(Boolean).map(w => w.at(0)?.toUpperCase() + w.slice(1).toLowerCase()).join(" ");
    }
}
