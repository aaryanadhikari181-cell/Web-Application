import React from 'react'

/**
 * Custom reusable Input component
 * Props:
 *  - label:       string  — label text above the input
 *  - type:        string  — input type (text, email, password, etc.)
 *  - name:        string  — input name attribute
 *  - value:       string  — controlled value
 *  - onChange:    func    — change handler
 *  - placeholder: string  — placeholder text
 *  - error:       string  — validation error message
 *  - required:    bool    — whether field is required
 */
const Input = ({
  label,
  type = 'text',
  name,
  value,
  onChange,
  placeholder = '',
  error = '',
  required = false,
}) => {
  return (
    <div className="input-wrapper">
      {label && (
        <label htmlFor={name} className="input-label">
          {label}
          {required && <span className="required-star"> *</span>}
        </label>
      )}

      <input
        id={name}
        type={type}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required={required}
        className={`input-field ${error ? 'input-error' : ''}`}
        autoComplete={type === 'password' ? 'current-password' : 'off'}
      />

      {error && <p className="error-msg">⚠ {error}</p>}
    </div>
  )
}

export default Input
