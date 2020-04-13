import React from 'react'
import classes from './MenuToggle.scss'

export function MenuToggle(props){
    console.log(classes)
    const cls = [
       classes.MenuToggle,
        'fa'
    ]
    console.log(cls)
    if (props.isOpen){
        cls.push('fa-times');
        cls.push(classes.open);
    } 
    else cls.push('fa-bars');

    return (
        <i className={cls.join(' ')} onClick={props.onToggle}></i>
    )
}