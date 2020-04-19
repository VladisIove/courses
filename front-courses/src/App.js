import React, {Component} from 'react';
import {Switch, Route} from 'react-router-dom'
import NavBar from './components/NavBar/NavBar';
import Home from './components/Home/Home';
import FAQ from './components/FAQ/FAQ';
import './App.css';

class App extends Component{

  render(){
    return (
      <div>
      <NavBar/>
      <Switch>
        <Route path="/" exact>
          <Home/>
        </Route>
        <Route path="/faq">
          <FAQ/>
        </Route>
      </Switch>
      </div>
    )
  }
}
/*
    <Switch>
      <Route path="/">
        <Home/>
      </Route>
      <Route path="/about">
        <About/>
      </Route>
      <Route path="/faq">
        <Faq/>
      </Route>
      <Route path="/help">
        <Help/>
      </Route>
      <Route path="/terms">
        <Terms/>
      </Route>
      <Route path="/404">
        <Eroor404/>
      </Route>
    </Switch>
    <Footer/>*/
export default App;
