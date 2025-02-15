import React from "react";
import styles from "./App.module.css";
import { Navbar, Container } from "react-bootstrap";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import SignUp from "./pages/registration/SignUp";
import SignIn from "./pages/registration/SignIn";
import "./App.css";

function App() {
  return (
    <Router>
      <div className={styles.App}>
        <Navbar bg="dark" variant="dark">
          <Container>
            <Navbar.Brand href="#home">Navbar</Navbar.Brand>
          </Container>
        </Navbar>
        <Container className={styles.Main}>
          <Routes>
            <Route path="/" element={<SignIn />} />
            <Route path="/signIn" element={<SignIn />} />
            <Route path="/signUp" element={<SignUp />} />
          </Routes>
        </Container>
      </div>
    </Router>
  );
}

export default App;
