import './register-page.sass';

import {useState} from "react";

const RegisterPage = () => {
  const [userEmail, setUserEmail] = useState("");
  const [userPassword, setUserPassword] = useState("");
  const [userSecondPassword, setUserSecondPassword] = useState("");
  const [userName, setUserName] = useState("");
  const [name, setName] = useState("");

  const onSubmitHandler = (event) => {
    event.preventDefault();
    console.log("Email: ", userEmail);
    setUserSecondPassword("");
    setUserPassword("");
    setUserEmail("");
    setUserName("");
    setName('');

  }



  return (
    <div className={'register'}>
      <h2>Register your account</h2>
      <form onSubmit={onSubmitHandler}>
        <div className={'form-item'}>
          <label htmlFor="name">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            required
            placeholder={'Enter your full name...'}
            value={name}
            onChange={e => setName(e.target.value)}/>
        </div>
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
        <div className={'form-item'}>
          <label htmlFor="username">Username</label>
          <input
            type={'text'}
            id={'username'}
            name={'username'}
            required
            placeholder={'Enter your Username'}
            value={ userName}
            onChange={e => setUserName(e.target.value)}/>
        </div>
        <div className={'form-item'}>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            name="password"
            required
            placeholder={'Enter your Password'}
            value={userPassword}
            onChange={e => setUserPassword(e.target.value)}/>
        </div>
        <div className={'form-item last'}>
          <label htmlFor="secondpassword">Password</label>
          <input
            type="password"
            id="secondpassword"
            name="secondpassword"
            required
            placeholder={'Repeat your password'}
            value={userSecondPassword}
            onChange={e => setUserSecondPassword(e.target.value)}/>
        </div>
        <button className={'form-button'} type="submit">Register</button>
      </form>
      <div className={'already'}>
        Already have an account? <a href={'/login'}>Login</a>
      </div>
    </div>
  );

}

export default RegisterPage;