import React from 'react';
import './App.css';
import Spam from './Spam'
import {Route,Routes} from 'react-router-dom'

function App() {
  return (
    <Routes>
      <Route path={'/'} element={
        <main>
          <Spam/>
        </main>
      } />
    </Routes> 


    
  );
}

export default App;
