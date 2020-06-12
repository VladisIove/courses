from apps.users.views import (LoginView, LogoutView, 
                        RegistrationView, AccessUserView, 
                        EditUserView, RemoveUserView, CreateUserView)

from apps.courses.views import AllCoursesView, RemoveCourseView, EditCourseView, CreateCourseView, AllFileView, CreateFileView, RemoveFileView, EditFileView
from apps.utils.views import AllFAQView, CreateFAQView, EditeFAQView, RemoveFAQView

def setup_routes(app):
    app.router.add_post('/courses', AllCoursesView, name='all_courses')
    app.router.add_post('/courses/edit', EditCourseView, name="edit_course")
    app.router.add_post('/courses/remove', RemoveCourseView, name="remove_course")
    app.router.add_post('/courses/create', CreateCourseView, name="create_course")
    
    app.router.add_post('/files', AllFileView, name='all_files')
    app.router.add_post('/files/edit', EditFileView, name='edit_file')
    app.router.add_post('/files/create', CreateFileView, name='create_file')
    app.router.add_post('/files/remove', RemoveFileView, name='remove_file')

    app.router.add_post('/users/login', LoginView, name='login')
    app.router.add_post('/users/logout', LogoutView, name='logout')
    app.router.add_post('/users/registration', RegistrationView, name='registration')
    app.router.add_post('/users/access_user', AccessUserView, name='access_user')
    app.router.add_post('/users/edit', EditUserView, name='edit_user')
    app.router.add_post('/users/remove', RemoveUserView, name='remove_user')
    app.router.add_post('/users/create', CreateUserView, name='create_user')
    
    app.router.add_post('/faqs', AllFAQView, name='all_faq')
    app.router.add_post('/faqs/create', CreateFAQView, name='create_faq')
    app.router.add_post('/faqs/edit', EditeFAQView, name='edit_faq')
    app.router.add_post('/faqs/remove', RemoveFAQView, name='remove_faq')