import React, { useState, useEffect } from 'react'
import logo from './logo.svg';
import './App.css';

function App() {
  const [initData, setInitData] = useState(null)

  useEffect(() => {
    fetch('/api').then(
      response => response.json()
    ).then(data =>
      // setInitData(data)
      // try that...
      setInitData(data.book_title)
      // console.log(data)
    )
  }, [])

  return (
    <div className="App">
      <header className="App-header">
        <img focusable={false} src={logo} className="icon" alt="logo" />
        <h1>{initData}</h1>
      </header>

    </div>
  );
}

export default App;
