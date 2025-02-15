
import React from "react";
import styles from "./App.module.css";
import Container from "react-bootstrap/Container";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignUp from "./pages/registration/SignUp";
import SignIn from "./pages/registration/SignIn";
import AboutPage from "./pages/About";
import NavBar from "./components/navbar";
import "./App.css";

function App() {

    return (
        <div className={styles.App}>
            <NavBar />
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
