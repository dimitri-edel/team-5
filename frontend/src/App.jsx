import styles from './App.module.css';
import NavBar from './components/NavBar';
import Container from 'react-bootstrap/Container';
import { Route, Routes } from "react-router-dom"
import  SignIn from './pages/registration/signIn';
import Register from './pages/registration/register';
import AboutPage from './pages/about'
import './App.css';

export default function App() {
return (
<div className={styles.App}>
 <NavBar/>
 <Container className={styles.Main}>
     <Routes>
          <Route path="/SignIn" element={<SignIn />} />
          <Route path="/Register" element={<Register />} />
          <Route path="/AboutPage" element={<AboutPage />} />
     </Routes>   
 </Container>
 
</div>

);
}
