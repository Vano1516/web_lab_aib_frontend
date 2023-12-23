import React from "react";
import ReactDOM from "react-dom/client";
import "./components/App.css";
import reportWebVitals from "./reportWebVitals";
import App from "./components/App.jsx";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();
