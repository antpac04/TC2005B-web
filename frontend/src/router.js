import { createBrowserRouter } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import About from "./pages/About";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <Dashboard />
  },
  {
    path: "/acerca-de",
    element: <About /> 
  }
]);
