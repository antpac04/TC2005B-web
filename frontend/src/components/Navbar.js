import React from 'react'
import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <>
      <header className="header">
        <h1 className="title">Space Adventures</h1>
        <nav className="navbar">
          <Link to="/">Gráficas</Link>
          <Link to="/acerca-de">Acerca de</Link>
        </nav>
      </header>
    </>
  )
}

export default Navbar