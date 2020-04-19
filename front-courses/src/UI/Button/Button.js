import React from 'react';
import {NavLink} from 'react-router-dom';
import classess from './Button.module.scss';

const Button = (props) => (
    <NavLink to={props.link} className={classess.Button}>{props.text}</NavLink>
)

export default Button;