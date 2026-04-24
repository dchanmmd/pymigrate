import { defineConfig } from "vite";
import path from "path";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
    plugins: [react(), tailwindcss()],
    resolve: {
        alias: {
            "@components": path.resolve(import.meta.dirname, "src/components"),
            "@styles": path.resolve(import.meta.dirname, "src/styles")
        }
    }
});
