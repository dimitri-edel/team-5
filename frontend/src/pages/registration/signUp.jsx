import React, { useState } from "react";
import { Link} from "react-router-dom";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import styles from "../../styles/signUpInForm.module.css";
import btnStyles from "../../styles/button.module.css";
import appStyles from "../../App.module.css";
import {
    Form,
    Button,
    Container,
    Alert,
} from "react-bootstrap";
const SignUp = () => {
    const [signUpData, setSignUpData] = useState({
        userEmail: "",
        password1: "",
        password2: "",
    });
    const { userEmail, password1, password2 } = signUpData;
    const [errors, setErrors] = useState({});
    const handleChange = (event) => {
        setSignUpData({
            ...signUpData,
            [event.target.name]: event.target.value,
        });
    };
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            // To Do ...
            // Post data to backend
        } catch (err) {
            setErrors(err.response?.data);
        }
    };
    return (
    <Container className={`${appStyles.SignInUpContainer} `}>
        <Row className={styles.Row}>
                    <h1 className={styles.Header}>sign up</h1>
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="userEmail">
                            <Form.Label className="d-none">userEmail</Form.Label>
                            <Form.Control
                                className={styles.Input}
                                type="email"
                                placeholder="userEmail"
                                name="userEmail"
                                value={userEmail}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.userEmail?.map((message, idx) => (
                            <Alert variant="warning" key={idx}>
                                {message}
                            </Alert>
                        ))}
                        <Form.Group controlId="password1">
                            <Form.Label className="d-none">Password</Form.Label>
                            <Form.Control
                                className={styles.Input}
                                type="password"
                                placeholder="Password"
                                name="password1"
                                value={password1}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.password1?.map((message, idx) => (
                            <Alert key={idx} variant="warning">
                                {message}
                            </Alert>
                        ))}
                        <Form.Group controlId="password2">
                            <Form.Label className="d-none">Confirm password</Form.Label>
                            <Form.Control
                                className={styles.Input}
                                type="password"
                                placeholder="Confirm password"
                                name="password2"
                                value={password2}
                                onChange={handleChange}
                            />
                        </Form.Group>
                        {errors.password2?.map((message, idx) => (
                            <Alert key={idx} variant="warning">
                                {message}
                            </Alert>
                        ))}
                        <Button
                            className={`${btnStyles.Button} ${btnStyles.Wide} ${btnStyles.Bright}`}
                            type="submit"
                        >
                            Sign up
                        </Button>
                        {errors.non_field_errors?.map((message, idx) => (
                            <Alert key={idx} variant="warning" className="mt-3">
                                {message}
                            </Alert>
                        ))}
                    </Form>                
                
                    <Link className={styles.Link} to="/signin">
                        Already have an account? <span>Sign in</span>
                    </Link>
                
        </Row>
        <Row>
            
        </Row>
     </Container>
        
    );

};

export default SignUpForm;