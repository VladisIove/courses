import React from 'react'
import Button from '../../../UI/Button/Button'
import classes from './Header.module.scss'

const Header = ()=>{
    console.log(classes)
    return (
        <header className={classes.Header}>
            <div className={classes.MainWords}>
                <p className={classes.MainWord}>Интенсивы, курсы, образование в один клик</p>
                <span className={classes.HeaderButtons}>
                <Button text="Зарегестрироваться" link="registration"/>
                <Button text="Войти" link="login"/>
                </span>
            </div>
            <div className={classes.BgImg}>
                <img src="https://images.unsplash.com/photo-1567176019833-b7063aa49069?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80"/>
            </div>
        </header>
    )   
    
}

export default Header;