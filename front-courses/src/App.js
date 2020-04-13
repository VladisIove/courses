import React from 'react';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import { Home } from './containers/Home/Home'
import {NavBar} from './containers/NavBar/NavBar'
import './App.css';

function App() {
  return (
    <Router>
      <NavBar/>
      <Switch>
        <Route path="/" exact>
          <Home/>
        </Route>
        
      </Switch>
    </Router>
  );
}

export default App;
