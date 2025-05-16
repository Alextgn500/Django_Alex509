import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

// Пример простых компонентов страниц
function Home() {
  return <h1>Главная страница</h1>;
}

function About() {
  return <h1>О нас</h1>;
}

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Главная</Link></li>
          <li><Link to="/about">О нас</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
