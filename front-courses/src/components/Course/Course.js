import React, {Component} from 'react';
import { connect } from 'react-redux';
import VideoBar from './VideoBar/VideoBar';
import VideoFrame from './VideoFrame/VideoFrame';
import {FILTER_COURSES_FUNCT} from '../../redux-courses/Courses/actions'

class Course extends Component{
    constructor(props){
        super(props);
        this.props.filterCourses(this.props.path.match.params.uuid)
    }

    render(){
        return (   
            <div>
                <div>
                    <img alt="img"/>
                    <div>

                    </div>
                </div>
                <div>
                <VideoFrame/>
                <VideoBar/>
                </div>
            </div>
        )
    }
}

const mapStateToProps = store => {
    return {
        course: store.reduserCourses
    }
}

const mapDispatchToProps = dispatch => {
    return {
        filterCourses: id => dispatch(FILTER_COURSES_FUNCT(id))
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(Course);
