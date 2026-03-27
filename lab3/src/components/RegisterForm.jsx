import React, { useState } from 'react'
import Input from './Input'

const RegisterForm = ({ onSwitch }) => {
  const [form, setForm] = useState({
    fullName: '',
    email: '',
    password: '',
    confirmPassword: '',
  })
  const [errors, setErrors] = useState({})
  const [success, setSuccess] = useState(false)

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
    setErrors((prev) => ({ ...prev, [name]: '' }))
  }

  const validate = () => {
    const errs = {}
    if (!form.fullName.trim()) errs.fullName = 'Full name is required.'
    else if (form.fullName.trim().length < 3) errs.fullName = 'Name must be at least 3 characters.'

    if (!form.email) errs.email = 'Email is required.'
    else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) errs.email = 'Enter a valid email address.'

    if (!form.password) errs.password = 'Password is required.'
    else if (form.password.length < 6) errs.password = 'Password must be at least 6 characters.'
    else if (!/[A-Z]/.test(form.password)) errs.password = 'Password must contain at least one uppercase letter.'

    if (!form.confirmPassword) errs.confirmPassword = 'Please confirm your password.'
    else if (form.password !== form.confirmPassword) errs.confirmPassword = 'Passwords do not match.'

    return errs
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const validationErrors = validate()
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors)
      return
    }
    setSuccess(true)
    console.log('Register data:', { ...form, password: '[HIDDEN]' })
  }

  if (success) {
    return (
      <div className="success-box">
        <div className="success-icon">🎉</div>
        <h2>Account Created!</h2>
        <p>Welcome, <strong>{form.fullName}</strong>! Your account has been registered.</p>
        <button className="btn-secondary" onClick={() => { setSuccess(false); setForm({ fullName: '', email: '', password: '', confirmPassword: '' }) }}>
          Register another
        </button>
      </div>
    )
  }

  return (
    <div className="form-card">
      <div className="form-header">
        <div class="form-icon">✨</div>
        <h2>Create Account</h2>
        <p>Join us — it's free!</p>
      </div>

      <form onSubmit={handleSubmit} noValidate>
        <Input
          label="Full Name"
          type="text"
          name="fullName"
          value={form.fullName}
          onChange={handleChange}
          placeholder="Aaryan Adhikari"
          error={errors.fullName}
          required
        />

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
          placeholder="Min. 6 chars, 1 uppercase"
          error={errors.password}
          required
        />

        <Input
          label="Confirm Password"
          type="password"
          name="confirmPassword"
          value={form.confirmPassword}
          onChange={handleChange}
          placeholder="Repeat your password"
          error={errors.confirmPassword}
          required
        />

        <button type="submit" className="btn-primary">
          Create Account →
        </button>
      </form>

      <p className="form-switch">
        Already have an account?{' '}
        <button className="link-btn" onClick={onSwitch}>Log in here</button>
      </p>
    </div>
  )
}

export default RegisterForm
