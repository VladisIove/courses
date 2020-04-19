import React from 'react';
import {connect} from 'react-redux';
import Button from '../../../UI/Button/Button'
import classes from './MainPart.module.scss';

const MainPart = (props) => (
    <div className={classes.Bg}>
        <p className={classes.NameBlock}>Наши курсы</p>
        <div className={classes.Courses}>
            {props.courses.map((e,i)=>{
                if(i%2){
                    return (
                        <div key={e.id} className={classes.Course}>
                            <div className={classes.Text}>
                                <p className={classes.Name}>{e.nameCourse}</p>
                                <p className={classes.Description}>{e.description}</p>
                                <Button text="Подробнее" link="description"/>
                            </div>
                            <div className={classes.Img}>
                                <img src={e.imgHref}/>
                            </div>
                        </div>
                    )
                }
                return (
                    <div key={e.id} className={classes.Course}>
                        <div className={classes.Img}>
                            <img src={e.imgHref}/>
                        </div>
                        <div className={classes.Text}>
                            <p className={classes.Name}>{e.nameCourse}</p>
                            <p className={classes.Description}>{e.description}</p>
                            <Button text="Подробнее" link="description"/>
                        </div>
                    </div>
                )
            })}
        </div>
    </div>
)

export default connect(state=>({courses: state.reduserCourses}))(MainPart);