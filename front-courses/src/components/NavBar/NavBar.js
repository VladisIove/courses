import React, {Component} from 'react';
import {NavLink} from 'react-router-dom'
import classes from './NavBar.module.scss'


export default class NavBar extends Component {

    componentDidMount() {
        window.addEventListener('scroll', this.handleScroll, { passive: true })
    }
    
    componentWillUnmount() {
        window.removeEventListener('scroll', this.handleScroll)
    }
    
    handleScroll(event){
        const header = document.querySelector(`.${classes.MainHeader}`);
        const scrollPos = window.scrollY;
        if(scrollPos>10){
            header.classList.add(classes.scrolled);
        }else header.classList.remove(classes.scrolled);
    }

    state = {
        navLinks: [
            {key: 'home', name: 'Главная', link: "/"},
            {key: 'about', name: 'О нас', link: "/about"},
            {key: 'faq', name: 'Частые вопрсоы', link: "/faq"},
            {key: 'login', name: 'Войти/Зарегестрироваться', link: "/login"},
        ]
    }

    ToggleCheckBox = () => {
        let check = document.getElementById("MenuBtnId");
        
        if(check.checked) check.checked = false; 
        else check.checked = true;
        console.log(check.checked )
    }

    render () {
        console.log(this.state.navLinks)
        return (
            <nav className={classes.MainHeader}>
                <div className={classes.logo}>
                    <NavLink to="/">Logo</NavLink>
                </div>

                <input type="checkbox" className={classes.MenuBtn} id="MenuBtnId"/>
                <label htmlFor="menuBtnId" className={classes.MenuIcon } onClick={this.ToggleCheckBox}>
                    <span className={classes.MenuIcon_line} ></span>
                </label>

                <ul className={classes.NavLinks}>
                    {this.state.navLinks.map(e=>(
                        <li className={classes.NavLink} key={e.key} onClick={this.ToggleCheckBox} >
                            <NavLink to={e.link} >{e.name}</NavLink>
                        </li>
                    ))}
                </ul>
            </nav>
        )
    }
}