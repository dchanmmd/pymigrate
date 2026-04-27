import { Component } from "@angular/core";
import { FormsModule } from "@angular/forms";
import { LoginService } from "./login.service";

@Component({
    selector: "app-login-view",
    standalone: true,
    imports: [FormsModule],
    templateUrl: "./login-view.html"
})
export class LoginView {
    username: string = "";
    password: string = "";
    showPassword: boolean = false;

    constructor(private loginService: LoginService) { }

    togglePassword(): void {
        this.showPassword = !this.showPassword;
    }

    submitLogin() {
        console.log({ username: this.username, password: this.password });
        // this.loginService.login({ 
        //     username: this.username, 
        //     password: this.password 
        // }).subscribe({
        //     next: (response) => {

        //     },
        //     error: (error) => {

        //     }
        // });
    }
}
