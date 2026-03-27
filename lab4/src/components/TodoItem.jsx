import React, { useState } from 'react'

/**
 * TodoItem — displays a single todo with edit/delete/toggle controls
 * Props:
 *  - todo:     { id, text, completed }
 *  - onToggle: (id) => void
 *  - onDelete: (id) => void
 *  - onEdit:   (id, newText) => void
 */
const TodoItem = ({ todo, onToggle, onDelete, onEdit }) => {
  const [isEditing, setIsEditing] = useState(false)
  const [editText, setEditText] = useState(todo.text)

  const handleSave = () => {
    const trimmed = editText.trim()
    if (!trimmed) return            // don't save empty
    onEdit(todo.id, trimmed)
    setIsEditing(false)
  }

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') handleSave()
    if (e.key === 'Escape') { setEditText(todo.text); setIsEditing(false) }
  }

  return (
    <li className={`todo-item ${todo.completed ? 'done' : ''}`}>
      {/* Checkbox */}
      <button
        className={`checkbox ${todo.completed ? 'checked' : ''}`}
        onClick={() => onToggle(todo.id)}
        title="Toggle complete"
      >
        {todo.completed ? '✓' : ''}
      </button>

      {/* Text or Edit input */}
      {isEditing ? (
        <input
          className="edit-input"
          value={editText}
          onChange={(e) => setEditText(e.target.value)}
          onKeyDown={handleKeyDown}
          autoFocus
        />
      ) : (
        <span className="todo-text" onDoubleClick={() => !todo.completed && setIsEditing(true)}>
          {todo.text}
        </span>
      )}

      {/* Actions */}
      <div className="todo-actions">
        {isEditing ? (
          <>
            <button className="action-btn save" onClick={handleSave} title="Save">💾</button>
            <button className="action-btn cancel" onClick={() => { setEditText(todo.text); setIsEditing(false) }} title="Cancel">✕</button>
          </>
        ) : (
          <>
            {!todo.completed && (
              <button className="action-btn edit" onClick={() => setIsEditing(true)} title="Edit">✏️</button>
            )}
            <button className="action-btn delete" onClick={() => onDelete(todo.id)} title="Delete">🗑️</button>
          </>
        )}
      </div>
    </li>
  )
}

export default TodoItem
