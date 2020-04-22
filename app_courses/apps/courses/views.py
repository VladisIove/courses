from aiohttp import web 
from .models import Course
from apps.users.models import File
from apps.classes import AllView, RemoveView, EditeView, CreateView


class AllCoursesView(AllView):
    model = Course 

class RemoveCourseView(RemoveView):
    model = Course

class EditCourseView(EditeView):
    model = Course

class CreateCourseView(CreateView):
    model = Course 

class AllFileView(AllView):
    model = File 

class RemoveFileView(RemoveView):
    model = File

class CreateFileView(CreateView):
    model = File
    
    async def post(self):
        data = self.request.json()
        if data.get('format_file', False):
            queryset = await self.model.create()
            queryset.url = self.model.save_file(data['file'], data['format_file'])
            await queryset.apply()
            return web.json_response(queryset.to_dict())
        else:
            return await super().post(self)

class EditFileView(EditeView):
    model = File
    
    async def post(self):
        data = self.request.json()
        if data.get('format_file', False):
            queryset = await self.model.get(self.model.id == data['id'])
            queryset.url = self.model.save_file(data['file'], data['format_file'])
            await queryset.apply()
            return web.json_response(queryset.to_dict())
        else:
            return await super().post(self)
