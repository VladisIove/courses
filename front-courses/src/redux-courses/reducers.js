import {combineReducers} from 'redux';
import reduserFAQ from './FAQ/FAQ';
import reduserCourses from './Courses/Courses';
import reducerVideos from './Videos/Videos';

export default combineReducers({
    reduserFAQ,
    reduserCourses,
    reducerVideos
})