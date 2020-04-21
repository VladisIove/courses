from aiohttp import web 
from .models import Course
from apps.users.models import File
from apps.classes import AllView


class CoursesView(AllView):
    model = Course 

class VideosView(AllView):
    model = File 

class CheckBoughtCourseView(web.View):
    
    async def post(self, request):
        pass 
