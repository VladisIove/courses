from aiohttp import web 
from .views import (LoginView, LogoutView, 
                        RegistrationView, AccessUserView, 
                        EditUserView, RemoveUserView, CreateUserView)

urlpatterns = [
    web.post('/users/login', LoginView, name='login'),
    web.post('/users/logout', LogoutView, name='logout'),
    web.post('/users/registration', RegistrationView, name='registration'),
    web.post('/users/access_user', AccessUserView, name='access_user'),
    web.post('/users/edit', EditUserView, name='edit_user'),
    web.post('/users/remove', RemoveUserView, name='remove_user'),
    web.post('/users/create', CreateUserView, name='create_user'),
]

