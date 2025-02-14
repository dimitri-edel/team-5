
import './index.css'
import App from './App.jsx'
import { AuthProvider } from './context/authProvider'


ReactDOM.render(
    <React.StrictMode>
      <Router>
        <AuthProvider>
          <App />
        </AuthProvider>
      </Router>
    </React.StrictMode>,
 document.getElementById("root")
);
