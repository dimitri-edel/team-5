import { useRef, useState, useEffect, useContext } from 'react';
import AuthContext from "./context/AuthProvider";
import axios from './api/axios';


// To Do ... Once the Backend is ready
//const LOGIN_URL = '/auth';

const signIn = () => {
    const { setAuth } = useContext(AuthContext);
    const userRef = useRef();
    const errRef = useRef();

	@@ -22,24 +19,21 @@ const signIn = () => {

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
	@@ -64,7 +58,7 @@ const signIn = () => {
                    <h1>You are logged in!</h1>
                    <br />
                    <p>
                        <a href="#">Go to Home</a>
                    </p>
                </section>
            ) : (
                <section>
                    <p ref={errRef} className={errMsg ? "errmsg" : "offscreen"} aria-live="assertive">{errMsg}</p>
                    <h1>Sign In</h1>
                    <form onSubmit={handleSubmit}>
                        <label htmlFor="userEmail">UserEmail:</label>
                        <input
                            type="email"
                            id="userEmail"
                            ref={userRef}
                            autoComplete="off"
                            onChange={(e) => setUserEmail(e.target.value)}
                            value={userEmail}
                            required
                        />
                        <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            onChange={(e) => setPwd(e.target.value)}
                            value={pwd}
                            required
                        />
                        <button>Sign In</button>
                    </form>
                    <p>
                        Need an Account?<br />
                        <span className="line">
                            {/*put router link here*/}
                            <a href="#">Sign Up</a>
                        </span>
                    </p>
                </section>
            )}
        </>
    )
}

export default signIn