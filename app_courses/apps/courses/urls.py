from aiohttp import web 
from .views import (AllCoursesView, RemoveCourseView, EditCourseView, CreateCourseView, 
                    AllFileView, CreateFileView, RemoveFileView, EditFileView)


urlpatterns = [
    web.post('/courses', AllCoursesView, name='all_courses'),
    web.post('/courses/edit', EditCourseView, name="edit_course"),
    web.post('/courses/remove', RemoveCourseView, name="remove_course"),
    web.post('/courses/create', CreateCourseView, name="create_course"),

    web.post('/files', AllFileView, name='all_files'),
    web.post('/files/edit', EditFileView, name='edit_file'),
    web.post('/files/create', CreateFileView, name='create_file'),
    web.post('/files/remove', RemoveFileView, name='remove_file'),
]
