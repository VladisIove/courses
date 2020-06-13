from aiohttp import web 
from .views import (AllCoursesView, RemoveCourseView, EditCourseView, CreateCourseView, 
                    AllCoursesVideosView,CreateCoursesVideosView,EditCoursesVideosView,RemoveCoursesVideosView,
                    AllFileView, CreateFileView, RemoveFileView, EditFileView)


urlpatterns = [
    web.post('/courses', AllCoursesView, name='all_courses'),
    web.post('/courses/edit', EditCourseView, name="edit_course"),
    web.post('/courses/remove', RemoveCourseView, name="remove_course"),
    web.post('/courses/create', CreateCourseView, name="create_course"),

    web.post('/coursesvideos', AllCoursesVideosView, name='all_courses_videos'),
    web.post('/coursesvideos/edit', EditCourseView, name="edit_course_videos"),
    web.post('/coursesvideos/remove', RemoveCourseView, name="remove_course_videos"),
    web.post('/coucoursesvideosrses/create', CreateCourseView, name="create_course_videos"),
    
    web.post('/files', AllFileView, name='all_files'),
    web.post('/files/edit', EditFileView, name='edit_file'),
    web.post('/files/create', CreateFileView, name='create_file'),
    web.post('/files/remove', RemoveFileView, name='remove_file'),
]
