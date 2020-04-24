import React from 'react';
import classes from './Input.module.scss'

const Input = (props) => (
    <div  className={' '.join(classes.Field, classes.Form_group, props.type_input)}>
        <input type={props.type}  className={classes.Form_field} placeholder={props.placeholder} name={props.name} id={props.id} required={props.required} />
        <label htmlFor={props.id}  className={classes.Form_label}>{props.placeholder}</label>
    </div>
);


export default Input;