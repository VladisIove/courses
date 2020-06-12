import {FILTER_COURSES, GET_COURSES} from './actions'

const stateCourses = [
    {
        id: 1, 
        imgHref: 'https://images.unsplash.com/photo-1544190932-e72dc8512a5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        nameCourse: 'Culpa laborum nostrud aliqua eu Lorem esse excepteur culpa id adipisicing.',
        description: 'Adipisicing excepteur et in non deserunt sunt. Commodo nulla enim commodo ullamco Lorem duis. Officia adipisicing nostrud magna culpa laborum in aliquip aliqua sunt anim occaecat et culpa eu. Incididunt proident ut occaecat nostrud cillum voluptate est est eu irure reprehenderit.'
    },
    {
        id: 2, 
        imgHref: 'https://images.unsplash.com/photo-1544190932-e72dc8512a5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        nameCourse: 'Culpa laborum nostrud aliqua eu Lorem esse excepteur culpa id adipisicing.',
        description: 'Adipisicing excepteur et in non deserunt sunt. Commodo nulla enim commodo ullamco Lorem duis. Officia adipisicing nostrud magna culpa laborum in aliquip aliqua sunt anim occaecat et culpa eu. Incididunt proident ut occaecat nostrud cillum voluptate est est eu irure reprehenderit.'
    },
    {
        id: 3, 
        imgHref: 'https://images.unsplash.com/photo-1544190932-e72dc8512a5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        nameCourse: 'Culpa laborum nostrud aliqua eu Lorem esse excepteur culpa id adipisicing.',
        description: 'Adipisicing excepteur et in non deserunt sunt. Commodo nulla enim commodo ullamco Lorem duis. Officia adipisicing nostrud magna culpa laborum in aliquip aliqua sunt anim occaecat et culpa eu. Incididunt proident ut occaecat nostrud cillum voluptate est est eu irure reprehenderit.'
    },
    {
        id: 4, 
        imgHref: 'https://images.unsplash.com/photo-1544190932-e72dc8512a5d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1267&q=80',
        nameCourse: 'Culpa laborum nostrud aliqua eu Lorem esse excepteur culpa id adipisicing.',
        description: 'Adipisicing excepteur et in non deserunt sunt. Commodo nulla enim commodo ullamco Lorem duis. Officia adipisicing nostrud magna culpa laborum in aliquip aliqua sunt anim occaecat et culpa eu. Incididunt proident ut occaecat nostrud cillum voluptate est est eu irure reprehenderit.'
    }
]

export default function Courses(courses=stateCourses, action){
    switch(action.type){
        case GET_COURSES:
            return courses
        case FILTER_COURSES:
            return courses.filter(e=>e.id===action.id)
        default:
            return courses
    }
}