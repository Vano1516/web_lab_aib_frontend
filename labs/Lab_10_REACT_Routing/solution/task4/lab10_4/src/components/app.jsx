import React from 'react';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';
import MainPage from './mainPage';
import AboutPage from './aboutPage';
import UserList from './userList';
import UserDetails from './userDetails';
const App = () => {
  return (
    <Router>
      <nav>
        <ul>
        <li>
            <Link to="/">Список пользователей</Link>
          </li>
          <li>
            <Link to="/main">Main</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>

        </ul>
      </nav>

      <Routes>
        <Route path="/main" element={<MainPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/" element={<UserList />} />
        <Route path="/users/:id" element={<UserDetails />} />
      </Routes>
    </Router>
  );
};

export default App;