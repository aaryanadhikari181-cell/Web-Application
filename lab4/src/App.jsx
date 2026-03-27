import React, { useState } from 'react'
import TodoItem from './components/TodoItem'

// Initial seed data
const INITIAL_TODOS = [
  { id: 1, text: 'Complete LAB 1 — Portfolio with Calendar', completed: true },
  { id: 2, text: 'Complete LAB 2 — Intro to JavaScript', completed: true },
  { id: 3, text: 'Complete LAB 3 — React Auth Forms', completed: false },
  { id: 4, text: 'Complete LAB 4 — Todo CRUD App', completed: false },
]

const FILTERS = ['All', 'Active', 'Completed']

const App = () => {
  // ===== STATE =====
  const [todos, setTodos]       = useState(INITIAL_TODOS)
  const [inputText, setInputText] = useState('')
  const [filter, setFilter]     = useState('All')
  const [error, setError]       = useState('')

  // ===== CREATE =====
  const handleAdd = (e) => {
    e.preventDefault()
    const text = inputText.trim()
    if (!text) { setError('Please enter a task.'); return }
    if (todos.some(t => t.text.toLowerCase() === text.toLowerCase())) {
      setError('This task already exists.'); return
    }
    const newTodo = {
      id: Date.now(),          // unique id from timestamp
      text,
      completed: false,
    }
    setTodos(prev => [newTodo, ...prev])
    setInputText('')
    setError('')
  }

  // ===== TOGGLE (complete/incomplete) =====
  const handleToggle = (id) => {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo
      )
    )
  }

  // ===== UPDATE =====
  const handleEdit = (id, newText) => {
    setTodos(prev =>
      prev.map(todo =>
        todo.id === id ? { ...todo, text: newText } : todo
      )
    )
  }

  // ===== DELETE =====
  const handleDelete = (id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id))
  }

  // ===== CLEAR COMPLETED =====
  const clearCompleted = () => {
    setTodos(prev => prev.filter(todo => !todo.completed))
  }

  // ===== MARK ALL COMPLETE =====
  const markAllComplete = () => {
    const allDone = todos.every(t => t.completed)
    setTodos(prev => prev.map(t => ({ ...t, completed: !allDone })))
  }

  // ===== FILTERED LIST =====
  const filtered = todos.filter(todo => {
    if (filter === 'Active')    return !todo.completed
    if (filter === 'Completed') return  todo.completed
    return true
  })

  const activeCount    = todos.filter(t => !t.completed).length
  const completedCount = todos.filter(t =>  t.completed).length

  return (
    <div className="app">
      {/* Header */}
      <header className="app-header">
        <h1>✅ Todo <span>CRUD</span></h1>
        <p>LAB 4 — React State Manipulation</p>
      </header>

      {/* Stats */}
      <div className="stats-bar">
        <div className="stat-chip">
          <span className="stat-num">{todos.length}</span>
          <span className="stat-lbl">Total</span>
        </div>
        <div className="stat-chip active">
          <span className="stat-num">{activeCount}</span>
          <span className="stat-lbl">Active</span>
        </div>
        <div className="stat-chip done">
          <span className="stat-num">{completedCount}</span>
          <span className="stat-lbl">Done</span>
        </div>
      </div>

      {/* Add form */}
      <form className="add-form" onSubmit={handleAdd}>
        <input
          className={`add-input ${error ? 'has-error' : ''}`}
          type="text"
          value={inputText}
          onChange={(e) => { setInputText(e.target.value); setError('') }}
          placeholder="Add a new task..."
        />
        <button type="submit" className="add-btn">+ Add</button>
      </form>
      {error && <p className="add-error">⚠ {error}</p>}

      {/* Filter tabs + bulk actions */}
      <div className="toolbar">
        <div className="filter-tabs">
          {FILTERS.map(f => (
            <button
              key={f}
              className={`filter-tab ${filter === f ? 'active' : ''}`}
              onClick={() => setFilter(f)}
            >
              {f}
            </button>
          ))}
        </div>
        <div className="bulk-actions">
          <button className="bulk-btn" onClick={markAllComplete} title="Toggle all">
            {todos.every(t => t.completed) ? '↺ Unmark All' : '✓ Mark All'}
          </button>
          {completedCount > 0 && (
            <button className="bulk-btn danger" onClick={clearCompleted}>
              🗑 Clear Done
            </button>
          )}
        </div>
      </div>

      {/* Todo list */}
      {filtered.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">
            {filter === 'Completed' ? '🏆' : filter === 'Active' ? '🎯' : '📝'}
          </div>
          <p>
            {filter === 'Completed' ? 'No completed tasks yet.'
              : filter === 'Active' ? 'All tasks are done! Great work!'
              : 'No tasks yet. Add one above!'}
          </p>
        </div>
      ) : (
        <ul className="todo-list">
          {filtered.map(todo => (
            <TodoItem
              key={todo.id}
              todo={todo}
              onToggle={handleToggle}
              onDelete={handleDelete}
              onEdit={handleEdit}
            />
          ))}
        </ul>
      )}

      {/* Footer hint */}
      <p className="hint">💡 Double-click a task to edit it</p>
    </div>
  )
}

export default App
