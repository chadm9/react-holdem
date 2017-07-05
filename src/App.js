import React, { Component } from 'react';
import './App.css';
import PokerTable from './customComponents/PokerTable'

class App extends Component {
  render() {
    return (
      <div className="Container">
        <PokerTable />
      </div>
    );
  }
}

export default App;
