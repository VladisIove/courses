from aiohttp import web

from app-courses.classes import EditeView, RemoveView


class LoginView(web.View):

    async def post(self, request):
        pass 

class LogoutView(web.View):

    async def post(self, request):
        pass 

class RegistrationView(web.View):

    async def post(self, request):
        pass 

class AccessUserView(web.View):

    async def post(self, request):
        pass 

class EditUserView(EditeView):
    model = User 

class RemoveUserView(RemoveView):
    model = User