import styles from './App.module.css';
import NavBar from 'react-bootstrap';
import Container from 'react-bootstrap';
import Route from 'react-router-dom';
import Switch from 'react-switch';
import signUp from './pages/registration/signUp';
import signIn from './pages/registration/signIn';
import './App.css';

function App() {
return (
<div className={styles.App}>
 <NavBar/>
 <Container className={styles.Main}>
   <Switch>
     <Route exact path='/signIn' render={() => <signIn />} />
     <Route exact path='/signUp' render={() => <signUp />} />
   </Switch>
  </Container>
 
</div>
 /*<div className="app">
      <h1>Team 5 API Demo</h1>
      <HelloWorld />
    </div>*/
);
}
export default App;