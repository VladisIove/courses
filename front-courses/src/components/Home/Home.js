import React, {Component} from 'react';
import Header from './Header/Header'
import MainPart from './MainPart/MainPart'
//import classes from './Home.scss';

export default class Home extends Component{

    render(){
        return (
            <>
                <Header/>
                <MainPart/>
            </>
        )   
    }
}