import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes } from "react-router";
import App from "./App.jsx";
import "@styles/index.css";
import "bootstrap-icons/font/bootstrap-icons.min.css";
import LoginView from "./views/LoginView.jsx";

createRoot(document.getElementById("root")).render(
    <StrictMode>
        <BrowserRouter>
            <Routes>
                
            </Routes>
        </BrowserRouter>
    </StrictMode>
);