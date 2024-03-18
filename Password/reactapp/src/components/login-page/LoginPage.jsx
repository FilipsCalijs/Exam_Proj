import {useState} from "react";
import './login-page.sass'
const LoginPage = () => {
  const [userEmail, setUserEmail] = useState('');
  const [userPassword, setUserPassword] = useState('');

  const onSubmitHandler = (event) => {
    event.preventDefault();
    console.log('Email: ', userEmail);
  }
  return (
    <div className={'login'}>
      <h2>Login to your account</h2>yo
      <form onSubmit={onSubmitHandler}>
        <div className={'form-item'}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            required
            placeholder={'Enter your email address...'}
            value={userEmail}
            onChange={e => setUserEmail(e.target.value)}/>
        </div>
        <div className={'form-item last'}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            required
            placeholder={'Enter your password...'}
            value={userPassword}
            onChange={e => setUserPassword(e.target.value)}/>
        </div>
        <div className={'form-item '}>
          <button type={'submit'}>Login</button>
        </div>
      </form>
      <div className="forgot">
        <a href={'/forgot-password'}>Forgot your password?</a>
      </div>
      <div className={'dont'}>
        Don't have an account? <a href={'/register'}>Register</a>
      </div>
    </div>
  )
}

export default LoginPage;