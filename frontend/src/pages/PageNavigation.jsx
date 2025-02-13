import { Link } from "react-router-dom";
import styles from './PageNavigation.module.css'

export default  function PageNavigation() {
    return (
        <nav className={styles.nav}>
            <ul>
                <li><Link to="/"> Home  </Link></li>
                <li><Link to="/signup">SignUp</Link></li>
                <li> <Link to="/login">SignIn</Link></li>
                <li><Link to="/logout">Log out</Link></li>
            </ul>
          
        </nav>
    )
}


