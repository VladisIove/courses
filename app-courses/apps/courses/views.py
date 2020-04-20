from aiohttp import web 
from apps-courses.classes import AllView


class CoursesView(AllView):
    model = Course 

class VideosView(AllView):
    model = File 

class CheckBoughtCourseView(web.View):
    
    async def post(self, request):
        pass 

class GetBoughtCourse(AllView):
    model = UserCourses