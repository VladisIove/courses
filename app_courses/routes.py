from apps.users.views import (LoginView, LogoutView, 
                        RegistrationView, AccessUserView, 
                        EditUserView, RemoveUserView)

from apps.courses.views import CoursesView, VideosView, CheckBoughtCourseView
from apps.utils.views import AllFAQView, CreateFAQView, EditeFAQView, RemoveFAQView

def setup_routes(app):
    app.router.add_post('/courses', CoursesView, name='all_courses')
    app.router.add_post('/videos', VideosView, name='all_videos')
    app.router.add_post('/users/login', LoginView, name='login')
    app.router.add_post('/users/logout', LogoutView, name='logout')
    app.router.add_post('/users/registration', RegistrationView, name='registration')
    app.router.add_post('/users/access_user', AccessUserView, name='access_user')
    app.router.add_post('/users/edit', EditUserView, name='edit_user')
    app.router.add_post('/users/remove', RemoveUserView, name='remove_user')
    app.router.add_post('/users/check_bought_course', CheckBoughtCourseView, name='check_bought_course')
    app.router.add_post('/faqs', AllFAQView, name='all_faq')
    app.router.add_post('/faqs/create', CreateFAQView, name='create_faq')
    app.router.add_post('/faqs/edit', EditeFAQView, name='edit_faq')
    app.router.add_post('/faqs/remove', RemoveFAQView, name='remove_faq')