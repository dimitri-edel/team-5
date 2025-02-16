import { useRef, useState, useEffect, useContext } from 'react';
import AuthContext from '../../context/authProvider';
import { Link} from "react-router-dom";
import axios from 'axios';
import { Row } from 'react-bootstrap';
import styles from "../../styles/signUpInForm.module.css";
import btnStyles from "../../styles/Button.module.css";
import appStyles from "../../App.module.css";
import {
    Form,
    Button,
    Container,
    Alert,
} from "react-bootstrap";
// To Do ... Once the Backend is ready
//const LOGIN_URL = '/auth';
const SignIn = () => {
    const { setAuth } = useContext(AuthContext);
    const userRef = useRef();
    const errRef = useRef();
    const [user, setUser] = useState('');
    const [userEmail, setUserEmail] = useState('');
    const [pwd, setPwd] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [user, pwd])
    const handleSubmit = async (e) => {
        e.preventDefault();
       /*
        try {
            const response = await axios.post(LOGIN_URL,
                JSON.stringify({ user, pwd }),
                {
                    headers: { 'Content-Type': 'application/json' },
                    withCredentials: true
                }
            );
            console.log(JSON.stringify(response?.data));
            
            const accessToken = response?.data?.accessToken;
            const roles = response?.data?.roles;
            setAuth({ userEmail, pwd, roles, accessToken });
            setUserEmail('');
            setPwd('');
            setSuccess(true);
        } catch (err) {
            if (!err?.response) {
                setErrMsg('No Server Response');
            } else if (err.response?.status === 400) {
                setErrMsg('Missing UserEmail or Password');
            } else if (err.response?.status === 401) {
                setErrMsg('Unauthorized');
            } else {
                setErrMsg('Login Failed');
            }
            errRef.current.focus();
        }*/
    }

    return (
        <Container className={`${appStyles.SignInUpContainer} `}>
        <Row className={styles.Row}>
                    <h1 className={styles.Header}>Sign in</h1>
        <>
            {success ? (
                <section>
                    <h1>You are logged in!</h1>
                    <br />
                    <p>
                        <a href="#">Go to Home</a>
                    </p>
                </section>
            ) : (
                <section>
                    <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    
                    <Form onSubmit={handleSubmit}>
                         <Form.Group controlId="userEmail">
                            <Form.Label className="d-none">userEmail</Form.Label>
                            <Form.Control
                                className={styles.Input}
                                type="email"
                                id="userEmail"
                                placeholder="userEmail"
                                ref={userRef}
                                autoComplete="off"
                                onChange={(e) => setUserEmail(e.target.value)}
                                value={userEmail}
                                required
                            />
                        </Form.Group>
                           

                        <Form.Group controlId="password">
                                <Form.Label className="d-none">Password</Form.Label>
                                <Form.Control
                                    className={styles.Input}
                                    type="password"
                                    id="password"
                                    placeholder="Password"
                                    onChange={(e) => setPwd(e.target.value)}
                                    value={pwd}
                                    required
                                />
                            </Form.Group>
                           
                            <Button
                                className={`${btnStyles.Button} ${btnStyles.Wide} ${btnStyles.Bright}`}
                                type="submit"
                            >
                                Sign in
                            </Button>
                           
                    </Form>
                    <Link className={styles.Link} to="/SignUp">
                        Need an account? <span>Sign Up</span>
                    </Link>
                </section>
            )}
        </>
        </Row>
        </Container>
    )
}

export default SignIn;