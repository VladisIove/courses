from aiohttp import web

from .models import User, Session
from apps.errors import DosntFoundQueryset, DosntValidId, DosntValidParameters, UserActivate, UserNotValidSession, GoodResponseUser, UserNotActive, UserNotValidPassOrEmail
from apps.classes import EditeView, RemoveView,CreateView, MixinClearQueryView, SendMessageOnEmail


class LoginView(MixinClearQueryView):

    async def post(self, request):
        data = await self.request.json()
        try:
            user = await User.get(email=data['email'])
            if user.active:
                return web.json_response({'state': UserNotActive.ERROR, 'description': UserNotActive.DESCRIPTION})
            if User.verify_password(user.password, data['password']):
                session = await Session.create(user_id=user.id, expired=False)
                return web.json_response(self.clear_query(session))   
            return web.json_response({'state': UserNotValidPassOrEmail.ERROR, 'description': UserNotValidPassOrEmail.DESCRIPTION})
        except User.DoesNotExist:
            return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class LogoutView(web.View):

    async def post(self, request):
        data = await self.request.json()
        try:
            user = await User.get(token=data['uuid'])
            session = await Session.get(token=data['token'])
            if session.user_id != user.id:
                return web.json_response({'state': UserNotValidSession.ERROR,'description': UserNotValidSession.DESCRIPTION})
            await session.update(expired=True).apply()
            return web.json_response({'state': GoodResponseUser.ERROR, 'description': GoodResponseUser.DESCRIPTION})
        except:
            return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class RemindPassword(web.View):

    async def post(self, request):
        data = await self.request.json()
        try:
            user = await User.get(email=data['email'])
            if user.active:
                session = await Session.create(user_id=user.id, expired=False)
                link = 'https://recreate_password/{}/{}'.format(user.uuid, session.token)
                subject = "Hi, {}! You are forgout your password? It is link to recreate password: {} ".format(user.name, link)
                SendMessageOnEmail(subject).send_message()
                return web.json_response({'state': UserNotActive.ERROR, 'description': UserNotActive.DESCRIPTION})
            return web.json_response({'state': UserNotActive.ERROR, 'description': UserNotActive.DESCRIPTION})      
        except:
            return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class RecreatePassword(web.View):

    async def post(self, request):
        data = await self.request.json()
        try:
            user = User.get(uuid=data['uuid'])
            session = Session.get(token=data['token'])
            if not user.active:
                return web.json_response({'state': UserNotActive.ERROR, 'description': UserNotActive.DESCRIPTION})
            if session.user_id != user.id or session.expired:
                return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})
            await user.update(password=User.hash_password(data['password']))
            return web.json_response({'state': GoodResponseUser.ERROR, 'description': GoodResponseUser.DESCRIPTION}) 
        except:
            return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})


class HelpMessage(web.View):

    async def post(self, request):
        data = await self.request.json()
        subject = "Name: {name}, email: {email}, \n message: {message}".format(**data)
        SendMessageOnEmail(subject).send_message()
        return web.json_response({'state': GoodResponseUser.ERROR, 'description': GoodResponseUser.DESCRIPTION})


class RegistrationView(web.View):

    async def post(self, request):
        try:
            await User.get(email=data['email'])
            return web.json_response({'state': UserActivate.ERROR, 'description': UserActivate.DESCRIPTION })
        except:
            user = await User.create(email=data['email'],
                                     password=User.hash_password(data['password']),
                                     active=False, 
                                     name="",
                                     second_name="",
                                     age=0,
                                     user_type=4)
            session = await Session.create(user_id=user.id, expired=False)
            link = 'https://activate/{}/{}'.format(user.uuid, session.token)
            subject = "Please activate your account: {}".format(link)
            SendMessageOnEmail(subject).send_message()
            return web.json_response({'state': GoodResponseUser.ERROR, 'description': GoodResponseUser.DESCRIPTION})

class AccessUserView(web.View):

    async def post(self, request):
        data = await self.request.json()
        try:
            user = await User.get(token=data['uuid'])
            session = await Session.get(token=data['token'])
            if session.user_id != user.id:
                return web.json_response({'state': UserNotValidSession.ERROR,'description': UserNotValidSession.DESCRIPTION})
            if user.active or session.expired:
                return web.json_response({'state': UserActivate.ERROR, 'description': UserActivate.DESCRIPTION })
            await user.update(active=True).apply()
            await session.update(expired=True).apply()
            return web.json_response({'state': GoodResponseUser.ERROR, 'description': GoodResponseUser.DESCRIPTION})
        except:
            return web.json_response({'state': DosntValidParameters.ERROR, 'description': DosntValidParameters.DESCRIPTION})

class EditUserView(EditeView):
    model = User 

class RemoveUserView(RemoveView):
    model = User

class CreateUserView(CreateView):
    model = User