from aiohttp import web 
from .models import CourseView, CourseVideo, ExerciseView, TestAnswer, BoughtCourses, CoursePackage
from apps.users.models import File
from apps.classes import AllView, RemoveView, EditeView, CreateView


class AllBoughtCoursesView(AllView):
    model = BoughtCourses

class RemoveBoughtCoursesView(RemoveView):
    model = BoughtCourses

class EditBoughtCoursesView(EditeView):
    model = BoughtCourses

class CreateBoughtCoursesView(CreateView):
    model = BoughtCourses

class AllExerciseView(AllView):
    model = ExerciseView

class EditExerciseView(EditeView):
    model = ExerciseView

class CreateExerciseView(CreateView):
    model = ExerciseView

class RemoveExerciseView(RemoveView):
    model = ExerciseView

class AllTestAnswer(AllView):
    model = TestAnswer

class EditTestAnswer(EditeView):
    model = TestAnswer

class RemoveTestAnswer(RemoveView):
    model = TestAnswer

class CreateTestAnswer(CreateView):
    model = TestAnswer

class AllCoursesView(AllView):
    model = CourseView 

class RemoveCourseView(RemoveView):
    model = CourseView

class EditCourseView(EditeView):
    model = CourseView

class CreateCourseView(CreateView):
    model = CourseView 

class AllCoursesVideosView(AllView):
    model = CourseVideo

class RemoveCoursesVideosView(RemoveView):
    model = CourseVideo

class EditCoursesVideosView(EditeView):
    model = CourseVideo

class CreateCoursesVideosView(CreateView):
    model = CourseVideo

class AllCoursePackageView(AllView):
    model = CoursePackage

class RemoveCoursePackageView(RemoveView):
    model = CoursePackage

class EditCoursePackageView(EditeView):
    model = CoursePackage

class CreateCoursePackageView(CreateView):
    model = CoursePackage


class AllFileView(AllView):
    model = File 

class RemoveFileView(RemoveView):
    model = File

class CreateFileView(CreateView):
    model = File
    '''
    async def post(self):
        data = self.request.json()
        if data.get('format_file', False):
            queryset = await self.model.create()
            queryset.url = self.model.save_file(data['file'], data['format_file'])
            await queryset.apply()
            return web.json_response(queryset.to_dict())
        else:
            return await super().post(self)
    '''

class EditFileView(EditeView):
    model = File
    '''
    async def post(self):
        data = self.request.json()
        if data.get('format_file', False):
            queryset = await self.model.get(self.model.id == data['id'])
            queryset.url = self.model.save_file(data['file'], data['format_file'])
            await queryset.apply()
            return web.json_response(queryset.to_dict())
        else:
            return await super().post(self)
    '''
