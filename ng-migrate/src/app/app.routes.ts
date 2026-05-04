import { Routes } from "@angular/router";
import { LoginView } from "./pages/login-view/login-view";
import { BranchView } from "./pages/branch-view/branch-view";
import { InventoryView } from "./pages/inventory-view/inventory-view";
import { JobView } from "./pages/job-view/job-view";

export const routes: Routes = [
    { path: "login", component: LoginView },
    { path: "branches", component: BranchView },
    { path: "branches/:id/inventory", component: InventoryView },
    { path: "transfers", component: JobView }
];
