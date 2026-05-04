import { HttpClient } from "@angular/common/http";
import { inject, Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { ListResponse } from "@common/interface/list-response.interface";
import { InventoryItem } from "@common/interface/inventory-item.interface";
import { environment } from "@environments/environment";
import { ItemResponse } from "@common/interface/item-response.interface";

@Injectable({ providedIn: "root" })
export class InventoryService {
    private readonly http: HttpClient = inject(HttpClient);

    public sendSelection(rowIds: string[]): Observable<ItemResponse<string>> {
        const payload = { rowIds };
        const url = new URL("/api/v1/transfers", environment.apiUrl);
        return this.http.post<ItemResponse<string>>(url.toString(), payload);
    } 
}