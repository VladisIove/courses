export const GET_VIEDOS_BY_COURSE = 'GET_VIEDOS_BY_COURSE';
export const GET_VIDEO_BY_ID = 'GET_VIDEO_BY_ID';

export default function getVideoByCourse(id_course){
    return {
        type: GET_VIEDOS_BY_COURSE,
        id_course: id_course
    }
}

export function getVideoById(id){
    return {
        type: GET_VIDEO_BY_ID,
        id: id
    }
}