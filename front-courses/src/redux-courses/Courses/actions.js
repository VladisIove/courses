export const GET_COURSES = 'GET_COURSES';
export const FILTER_COURSES = 'FILTER_COURSES';

export function FILTER_COURSES_FUNCT (id) {
    return {
        type: FILTER_COURSES,
        id: id
    } 
}