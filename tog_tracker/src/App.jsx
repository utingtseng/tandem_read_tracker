import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Nav from 'react-bootstrap/Nav';
import Home from './pages/Home';

function App() {

  return (
    <>
    <BrowserRouter>
      <Routes>
          <Route path="/" element={<Home />} />
      </Routes>
    </BrowserRouter>
    </>
  )
}

export default App
