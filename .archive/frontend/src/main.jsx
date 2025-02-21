import React from "react";

import ReactDOM from "react-dom/client";
import './index.css'
import App from './App.jsx';
import { BrowserRouter as Router } from "react-router-dom";
import { AuthProvider } from './context/authProvider.jsx'
import './styles/button.module.css';


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
        <AuthProvider>
          <App />
        </AuthProvider>
      </Router>
  </React.StrictMode>
);
