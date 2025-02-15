import { useRef, useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

// To Do ... Once the Backend is ready
//const LOGIN_URL = '/auth';

const SignIn = () => {
    const userRef = useRef();
    const errRef = useRef();

    const [userEmail, setUserEmail] = useState('');
    const [pwd, setPwd] = useState('');
    const [errMsg, setErrMsg] = useState('');
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        userRef.current.focus();
    }, [])

    useEffect(() => {
        setErrMsg('');
    }, [userEmail, pwd])

    const handleSubmit = async (e) => {
        e.preventDefault();
       /*
        try {
            const response = await axios.post(LOGIN_URL,
                JSON.stringify({ userEmail, pwd }),
                {
                    headers: { 'Content-Type': 'application/json' },
                    withCredentials: true
                }
            );
            console.log(JSON.stringify(response?.data));
            
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
        <>
            {success ? (
                <section>
                    <h1>You are logged in!</h1>
                    <br />
                    <p>
                        <Link to="/">Go to Home</Link>
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
                            <Link to="/signup">Sign Up</Link>
                        </span>
                    </p>
                </section>
            )}
        </>
    )
}

export default SignIn