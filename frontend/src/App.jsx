import styles from './App.module.css';
import NavBar from 'react-bootstrap';
import Container from 'react-bootstrap';
import Route from 'react-router-dom';
import Switch from 'react-switch';
import './App.css'
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
    /*<div className="app">
      <h1>Team 5 API Demo</h1>
      <HelloWorld />
    </div>*/
);
}


export default App;
