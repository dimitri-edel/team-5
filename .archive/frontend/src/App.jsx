
import React from "react";
import styles from "./App.module.css";
import Container from "react-bootstrap/Container";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignUp from "./pages/registration/signUp";
import SignIn from "./pages/registration/signIn";
import AboutPage from "./pages/About";
import NavBar from "./components/navbar";
import TestButton from "./components/TestButton";
import "./App.css";

function App() {

    return (
        <div className={styles.App}>
            <NavBar />
            <TestButton />
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
