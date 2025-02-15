import { Link } from "react-router"
import PageNavigation from "../components/PageNavigation"
import styles from './Home.module.css'
export default function Home() {
    return (
        <>
        
       <div className={styles.home}>
       {/* <PageNavigation className={styles.nav} /> */}

        <h3>Looking for a partner? </h3>
        <p>Click to get started...</p>
       
        <Link to="/signup" className={styles.link} >Get STARTED</Link>
       </div>
      
       </>
        
    )
}


