import React, { useState } from 'react'
import LoginForm from './components/LoginForm'
import RegisterForm from './components/RegisterForm'

const App = () => {
  // State to toggle between login and register views
  const [view, setView] = useState('login') // 'login' | 'register'

  return (
    <div className="app-container">
      <div className="app-brand">
        <h1>🔐 Auth<span>Lab</span></h1>
        <p>LAB 3 — React Forms & Custom Components</p>
      </div>

      {/* Tab switcher */}
      <div className="tab-bar">
        <button
          className={`tab ${view === 'login' ? 'tab-active' : ''}`}
          onClick={() => setView('login')}
        >
          Login
        </button>
        <button
          className={`tab ${view === 'register' ? 'tab-active' : ''}`}
          onClick={() => setView('register')}
        >
          Register
        </button>
      </div>

      {/* Render the active form */}
      {view === 'login'
        ? <LoginForm    onSwitch={() => setView('register')} />
        : <RegisterForm onSwitch={() => setView('login')} />
      }
    </div>
  )
}

export default App
