import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import Home from './pages/Home';
import SingleTask from './pages/SingleTask';
import UpdateTask from './pages/UpdateTask';
import './bootstrap.css';

function App() {

  return (
    <>
      <Router>
        <nav>
          <Link to="/">Home</Link>
        </nav>
        <Routes>
          <Route>
            <Route exact path="/" element={<Home />} />
            <Route path='task/:id/' element={<SingleTask />} />
            <Route path='edit/:id/' element={<UpdateTask />} />
          </Route>
        </Routes>
      </Router>
    </>
  )
}

export default App
