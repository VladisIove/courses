from apps.courses.urls import urlpatterns as CoursesUrls
from apps.utils.urls import urlpatterns as UtilsUrls
from apps.users.urls import urlpatterns as UsersUrls

def setup_routes(app):
    app.add_routes(CoursesUrls)
    app.add_routes(UsersUrls)
    app.add_routes(UtilsUrls)