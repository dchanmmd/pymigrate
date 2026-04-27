import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { environment } from "../../../environments/environment";

interface LoginRequest {
    username: string;
    password: string;
}

interface LoginResponse {
    // TODO utilizar shape de la respuesta de la API mmdpawn
}

@Injectable({ providedIn: "root" })
export class LoginService {
    constructor(private readonly http: HttpClient) { }

    login(data: LoginRequest): Observable<any> {
        const url = new URL("/api/v1/auth/login", environment.apiUrl);
        return this.http.post<LoginResponse>(url.toString(), data);
    }
}