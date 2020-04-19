import {combineReducers} from 'redux';
import reduserFAQ from './FAQ/FAQ';
import reduserCourses from './Courses/Courses';


export default combineReducers({
    reduserFAQ,
    reduserCourses,
})