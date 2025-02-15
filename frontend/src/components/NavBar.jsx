import styles from '../styles/NavBar.module.css';
import { NavLink } from 'react-router-dom';
import React from "react";
import { Container, Nav, Navbar } from "react-bootstrap";


const NavBar = () => {
    return (
        <Navbar
            className={styles.NavBar}
            expand="lg"
            fixed="top"
        >
            <Container fluid> 
                <Navbar>
                    <Nav className="mr-auto">
                        <NavLink
                            exact
                            className={styles.NavLink}
                            activeClassName={styles.Active}
                            to="/"
                        >
                            <i className="fas fa-home"></i>Home
                        </NavLink>
                        <NavLink
                            exact
                            className={styles.NavLink}
                            activeClassName={styles.Active}
                            to="/AboutPage"
                        >
                            <i className="fas fa-info"></i>About Us
                        </NavLink>

                        <NavLink
                            exact
                            className={styles.NavLink}
                            activeClassName={styles.Active}
                            to="/SignIn"
                        >
                            <i className="fas fa-info"></i>Sign In
                        </NavLink>

                        <NavLink
                            exact
                            className={styles.NavLink}
                            activeClassName={styles.Active}
                            to="/Register"
                        >
                            <i className="fas fa-info"></i>Sign Up
                        </NavLink>
                    </Nav>
                </Navbar>
            </Container>
        </Navbar>
    );
};

export default NavBar;