import { Link } from "react-router-dom";
import styles from './PageNavigation.module.css'

export default  function PageNavigation() {
    return (
        <nav className={styles.nav}>
           <Link to="/" >Home Page</Link>
           <Link to="/signup">Sign up</Link>
           <Link to="/login">Log in</Link>
           <Link to="/logout">Log out</Link>
        </nav>
    )
}


