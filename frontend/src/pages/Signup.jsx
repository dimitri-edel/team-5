import { Link } from "react-router-dom";
import PageNavigation from "./PageNavigation";

export default function Signup() {
    return (
        <div>
             <PageNavigation />
            

            <form>
                <h3>Have an account? <Link to="/login" >Signin</Link></h3>
                
                <label htmlFor="">Email</label>
                <input type="text" placeholder="Start typing..." />
                <label htmlFor="password">Password</label>
                <input type="password" placeholder="********" />
                <label htmlFor="confirmPassword">Confirm Password</label>
                <input type="password" placeholder="********" />
            </form>
        </div>
    )
}


