from aiohttp import web 
from apps.classes import AllView
from .models import FAQ 

class AllFAQView(AllView):
    model = FAQ

class CreateFAQView(web.View):
    model = FAQ 

class EditeFAQView(web.View):
    model = FAQ 

class RemoveFAQView(web.View):
    model = FAQ