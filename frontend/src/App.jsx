import './App.css';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom'
import Home from './pages/Home';
import SingleTask from './pages/SingleTask';
import UpdateTask from './pages/UpdateTask';
import CreateTask from './pages/CreateTask';
import './bootstrap.css';
import NotFound from './pages/NotFound';

function App() {

  return (
    <>
      <Router>
        <nav className='nav-bar'>
          <NavLink id='navlink' to="/">Home</NavLink>
          <NavLink id='navlink' to="/create">Create Task</NavLink>
        </nav>
        <Routes>
          <Route>
            <Route exact path="/" element={<Home />} />
            <Route path='/create' element={<CreateTask />} />
            <Route path='task/:id/' element={<SingleTask />} />
            <Route path='edit/:id/' element={<UpdateTask />} />
            <Route path='*' element={<NotFound />} />
          </Route>
        </Routes>
      </Router>
    </>
  )
}

export default App
