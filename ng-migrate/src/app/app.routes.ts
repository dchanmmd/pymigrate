import { Routes } from "@angular/router";
import { LoginView } from "./pages/login-view/login-view";
import { BranchView } from "./pages/branch-view/branch-view";
import { InventoryView } from "./pages/inventory-view/inventory-view";
import { TransferView } from "./pages/transfer-view/transfer-view";

export const routes: Routes = [
    { path: "", redirectTo: "login", pathMatch: "full" },
    { path: "login", component: LoginView },
    { path: "branches", component: BranchView },
    { path: "branches/:id/inventory", component: InventoryView },
    { path: "transfers", component: TransferView }
];
