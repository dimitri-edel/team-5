import Home from "./pages/Home"
import Login from "./pages/Login"
import Logout from "./pages/Logout"
import PageNotFound from "./pages/PageNotFound"
import Signup from "./pages/Signup"
import { BrowserRouter,Routes,Route } from "react-router-dom"

function App() {
  

  return (

    <>
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="signup" element={<Signup />} />
      <Route path="login" element={<Login />} />
      <Route path="logout" element={<Logout />} /> 
      <Route path="*" element={<PageNotFound />} /> 

    </Routes>
    </BrowserRouter>
    
   </>

   
  )
}

export default App
