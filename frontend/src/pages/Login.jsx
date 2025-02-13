import PageNavigation from "./PageNavigation";
import { Link } from "react-router-dom";

export default function Login() {
    return (
        <div>
             <PageNavigation />
             <form>
                <h3>Have no account? <Link>Sign Up</Link></h3>
                
                <label htmlFor="">Email</label>
                <input type="text" placeholder="Start typing..." />
                <label htmlFor="password">Password</label>
                <input type="password" placeholder="********" />
                
            </form>
        </div>
    )
}


