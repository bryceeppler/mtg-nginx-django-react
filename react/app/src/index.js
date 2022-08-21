import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import Bulk from "./Bulk";
import { ThemeProvider, createTheme, CssBaseline } from "@mui/material";

import { BrowserRouter, Routes, Route } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));

const theme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      // main: '#8C67AB',
      // main: '#3401A9',
      // main: '#00B0F0',
      // main: '#ECA35B',
      // main: '#0C90F2',
      main: "#1A6ED6",
    },
  },
});

root.render(
  <ThemeProvider theme={theme}>
    <CssBaseline />

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/bulk" element={<Bulk />} />
      </Routes>
    </BrowserRouter>
  </ThemeProvider>
);
