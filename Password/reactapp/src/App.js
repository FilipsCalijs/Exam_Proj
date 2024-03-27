import './App.css';
import RegisterPage from "./components/register-page/RegisterPage";
import LoginPage from "./components/login-page/LoginPage";
import PasswordManagementPage from "./components/password-management-page/PasswordManagementPage";

function App() {
  return (
    <div className="App">
      <PasswordManagementPage/>
    </div>
  );
}

export default App;
