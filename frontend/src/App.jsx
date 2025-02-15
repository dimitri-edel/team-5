
import React from "react";
import styles from "./App.module.css";
import { Navbar, Container } from "react-bootstrap";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignUp from "./pages/registration/SignUp";
import SignIn from "./pages/registration/SignIn";
import "./App.css";

function App() {

  return (
    <div className={styles.App}>
       <NavBar/>
        <Container className={styles.Main}>
            <Routes>
                <Route path="/SignIn" element={<SignIn />} />
                <Route path="/SignUp" element={<SignUp />} />
                <Route path="/AboutPage" element={<AboutPage />} />
            </Routes>   
        </Container>
        
    </div>
 
);
}



export default App;
