import styles from './App.module.css';
import { Navbar as NavBar } from 'react-bootstrap';
import { Container } from 'react-bootstrap';
import { Route, Routes } from 'react-router-dom';
import SignUp from './pages/registration/SignUp';
import SignIn from './pages/registration/SignIn';
import './App.css';

function App() {
  return (
    <div className={styles.App}>
      <NavBar />
      <Container className={styles.Main}>
        <Routes>
          <Route path='/signin' element={<SignIn />} />
          <Route path='/signup' element={<SignUp />} />
        </Routes>
      </Container>
    </div>
  );
}

export default App;