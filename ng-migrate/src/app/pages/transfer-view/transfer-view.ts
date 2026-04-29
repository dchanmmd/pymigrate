import { Component, inject, Signal } from "@angular/core";
import { Header } from "@app/components/header/header";
import { TransferJobCard } from "@app/components/transfer-job-card/transfer-job-card";
import { TransferService } from "./transfer.service";
import { JobSummary } from "@app/common/interface/job-summary.interface";
import { toSignal } from "@angular/core/rxjs-interop";
import { map } from "rxjs";

@Component({
    selector: "app-transfer-view",
    imports: [Header, TransferJobCard],
    templateUrl: "./transfer-view.html"
})
export class TransferView {
    private readonly transferService: TransferService = inject(TransferService);

    public jobs: Signal<Array<JobSummary>> = toSignal(
        this.transferService.fetchJobList().pipe(map(response => response.data)),
        { initialValue: [] }
    );
}
