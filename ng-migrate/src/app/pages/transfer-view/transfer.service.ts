import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { JobSummary } from "@common/interface/job-summary.interface";
import { ListResponse } from "@common/interface/list-response.interface";
import { environment } from "@environments/environment";
import { Observable } from "rxjs";

@Injectable({ providedIn: "root" })
export class TransferService {
    constructor(private readonly http: HttpClient) { }

    public fetchJobList(): Observable<ListResponse<JobSummary>> {
        const url = new URL(`/api/v1/transfers`, environment.apiUrl);
        return this.http.get<ListResponse<JobSummary>>(url.toString());
    }
}