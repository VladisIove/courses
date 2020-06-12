import {GET_VIEDOS_BY_COURSE, GET_VIDEO_BY_ID} from './action';

const videosState = [];

export default function reducerVideos(videos=videosState, action){
    switch (action.type){
        case GET_VIEDOS_BY_COURSE:
            return videos.filter(e => e.id_course === action.id_course)
        case GET_VIDEO_BY_ID:
            return videos.filter(e => e.id===action.id)
        default:
            return videos
    }

}