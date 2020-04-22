from aiohttp import web 
from apps.classes import AllView, CreateView, EditeView, RemoveView
from .models import FAQ 

class AllFAQView(AllView):
    model = FAQ

class CreateFAQView(CreateView):
    model = FAQ 

class EditeFAQView(EditeView):
    model = FAQ 

class RemoveFAQView(RemoveView):
    model = FAQ