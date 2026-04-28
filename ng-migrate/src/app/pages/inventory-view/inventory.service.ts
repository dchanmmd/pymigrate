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

    public fetchItem(branchId: string, itemId: string): Observable<ItemResponse<InventoryItem>> {
        const url = new URL(`/api/v1/inventory/${branchId}/${itemId}`, environment.apiUrl);
        return this.http.get<ItemResponse<InventoryItem>>(url.toString());
    }

    public fetchInventory(branchId: string, page: number = 1, query?: string): Observable<ListResponse<InventoryItem>> {
        console.log("FETCH INVENTORY")
        const url = new URL(`/api/v1/inventory/${branchId}`, environment.apiUrl);
        url.searchParams.set("page", page.toString());
        if (query) url.searchParams.set("query", query);
        
        return this.http.get<ListResponse<InventoryItem>>(url.toString());
    }

    public sendSelection(rowIds: string[]): Observable<ItemResponse<string>> {
        const payload = { rowIds };
        const url = new URL("/api/v1/transfers", environment.apiUrl);
        return this.http.post<ItemResponse<string>>(url.toString(), payload);
    } 
}