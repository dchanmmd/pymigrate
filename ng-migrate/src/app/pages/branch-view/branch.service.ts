import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { ListResponse } from "../../common/interface/list-response.interface";
import { Branch } from "../../common/interface/branch.interface";
import { environment } from "../../../environments/environment";

@Injectable({ providedIn: "root" })
export class BranchService {
    private readonly http: HttpClient = inject(HttpClient);

    public fetchBranchList(): Observable<ListResponse<Branch>> {
        const url = new URL("/api/v1/branches", environment.apiUrl);
        return this.http.get<ListResponse<Branch>>(url.toString());
    }
}