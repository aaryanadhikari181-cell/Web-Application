import React, { useState } from 'react'
import Input from './Input'

const LoginForm = ({ onSwitch }) => {
  // Controlled form state
  const [form, setForm] = useState({ email: '', password: '' })
  const [errors, setErrors] = useState({})
  const [success, setSuccess] = useState(false)

  // Generic change handler — works for any field
  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
    // Clear error on change
    setErrors((prev) => ({ ...prev, [name]: '' }))
  }

  // Validate fields
  const validate = () => {
    const newErrors = {}
    if (!form.email) {
      newErrors.email = 'Email is required.'
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
      newErrors.email = 'Enter a valid email address.'
    }
    if (!form.password) {
      newErrors.password = 'Password is required.'
    } else if (form.password.length < 6) {
      newErrors.password = 'Password must be at least 6 characters.'
    }
    return newErrors
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const validationErrors = validate()
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      return
    }
    // Simulate login success
    setSuccess(true)
    console.log('Login data:', form)
  }

  if (success) {
    return (
      <div className="success-box">
        <div className="success-icon">✅</div>
        <h2>Login Successful!</h2>
        <p>Welcome back, <strong>{form.email}</strong></p>
        <button className="btn-secondary" onClick={() => { setSuccess(false); setForm({ email: '', password: '' }) }}>
          Log out
        </button>
      </div>
    )
  }

  return (
    <div className="form-card">
      <div className="form-header">
        <div className="form-icon">🔐</div>
        <h2>Welcome Back</h2>
        <p>Log in to your account</p>
      </div>

      <form onSubmit={handleSubmit} noValidate>
        <Input
          label="Email Address"
          type="email"
          name="email"
          value={form.email}
          onChange={handleChange}
          placeholder="you@example.com"
          error={errors.email}
          required
        />

        <Input
          label="Password"
          type="password"
          name="password"
          value={form.password}
          onChange={handleChange}
          placeholder="Enter your password"
          error={errors.password}
          required
        />

        <button type="submit" className="btn-primary">
          Login →
        </button>
      </form>

      <p className="form-switch">
        Don't have an account?{' '}
        <button className="link-btn" onClick={onSwitch}>Register here</button>
      </p>
    </div>
  )
}

export default LoginForm
