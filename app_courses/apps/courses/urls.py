from aiohttp import web 
from .views import (AllCoursesView, RemoveCourseView, EditCourseView, CreateCourseView, 
                    AllCoursesVideosView,CreateCoursesVideosView,EditCoursesVideosView,RemoveCoursesVideosView,
                    AllFileView, CreateFileView, RemoveFileView, EditFileView,
                    AllBoughtCoursesView,RemoveBoughtCoursesView,EditBoughtCoursesView,CreateBoughtCoursesView,
                    AllExerciseView,EditExerciseView,CreateExerciseView,RemoveExerciseView,
                    AllTestAnswer, EditTestAnswer, RemoveTestAnswer, CreateTestAnswer,
                    AllCoursePackageView,RemoveCoursePackageView,EditCoursePackageView,CreateCoursePackageView,)


urlpatterns = [
    web.post('/courses', AllCoursesView, name='all_courses'),
    web.post('/courses/edit', EditCourseView, name="edit_course"),
    web.post('/courses/remove', RemoveCourseView, name="remove_course"),
    web.post('/courses/create', CreateCourseView, name="create_course"),

    web.post('/coursesvideos', AllCoursesVideosView, name='all_courses_videos'),
    web.post('/coursesvideos/edit', EditCourseView, name="edit_course_videos"),
    web.post('/coursesvideos/remove', RemoveCourseView, name="remove_course_videos"),
    web.post('/coursesvideos/create', CreateCourseView, name="create_course_videos"),
    
    web.post('/coursepackage', AllCoursePackageView, name='all_course_package'),
    web.post('/coursepackage/edit', EditCoursePackageView, name="edit_course_package"),
    web.post('/coursepackage/remove', RemoveCoursePackageView, name="remove_course_package"),
    web.post('/coursepackage/create', CreateCoursePackageView, name="create_course_package"),
    
    web.post('/files', AllFileView, name='all_files'),
    web.post('/files/edit', EditFileView, name='edit_file'),
    web.post('/files/create', CreateFileView, name='create_file'),
    web.post('/files/remove', RemoveFileView, name='remove_file'),

    web.post('/bought_courses', AllBoughtCoursesView, name='all_bought_courses'),
    web.post('/bought_courses/edit', EditBoughtCoursesView, name='edit_bought_courses'),
    web.post('/bought_courses/create', CreateBoughtCoursesView, name='create_bought_courses'),
    web.post('/bought_courses/remove', RemoveBoughtCoursesView, name='remove_bought_courses'),

    web.post('/exercise_view', AllExerciseView, name='all_exercise_view'),
    web.post('/exercise_view/edit', EditExerciseView, name='edit_exercise_view'),
    web.post('/exercise_view/create', CreateExerciseView, name='create_exercise_view'),
    web.post('/exercise_view/remove', RemoveExerciseView, name='remove_exercise_view'),

    web.post('/test_answer', AllTestAnswer, name='all_test_answer'),
    web.post('/test_answer/edit', EditTestAnswer, name='edit_test_answer'),
    web.post('/test_answer/create', CreateTestAnswer, name='create_test_answer'),
    web.post('/test_answer/remove', RemoveTestAnswer, name='remove_test_answer'),
]
