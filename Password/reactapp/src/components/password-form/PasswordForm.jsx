import settings from './Setting_linetest.svg';
import './password-form.sass';
const PasswordForm = () => {
  return (
    <aside className={'add-password'}>
      <h3>Add password</h3>
      <div className={'settings'}>
        <img src={settings} alt="set"/>
        <div className="settings-text">
          Andrejs Granenko
        </div>
      </div>
    </aside>
  )
}

export default PasswordForm;