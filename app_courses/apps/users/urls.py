from aiohttp import web 
from .views import (LoginView, LogoutView, HelpMessage,RemindPassword,
                        RegistrationView, AccessUserView,RecreatePassword, 
                        EditUserView, RemoveUserView, CreateUserView)

urlpatterns = [
    web.post('/users/login', LoginView, name='login'),
    web.post('/remind/password', RemindPassword, name='remind_password'),
    web.post('/recreate/password', RecreatePassword, name='recreate_password'),
    web.post('/help/message', HelpMessage, name='help_message'),
    web.post('/users/logout', LogoutView, name='logout'),
    web.post('/users/registration', RegistrationView, name='registration'),
    web.post('/users/access_user', AccessUserView, name='access_user'),
    web.post('/users/edit', EditUserView, name='edit_user'),
    web.post('/users/remove', RemoveUserView, name='remove_user'),
    web.post('/users/create', CreateUserView, name='create_user'),
]

