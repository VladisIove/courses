from apps.init_db import db


class AbstractCourse():

    class TYPE_COURSE:
        PYTHON = 1
        THREED_MAX = 2

    id = db.Column(db.Integer(), primary_key=True)
    name_course = db.Column(db.String())
    description = db.Column(db.String())
    author_id = db.Column(None, db.ForeignKey('users.id'), nullable=True)
    date = db.Column(db.DateTime())
    price = db.Column(db.Integer())
    old_price = db.Column(db.Integer())
    type_course = db.Column(db.Integer())
    data = db.Column(db.JSON())

class CoursePackage(db.Model, AbstractCourse):
    __tablename__ = 'courses_packages'


class CourseView(db.Model, AbstractCourse):
    __tablename__ = 'courses_view'

    package_id = db.Column(None, db.ForeignKey('courses_packages.id'), nullable=True)


class CourseVideo(db.Model):
    __tablename__ = 'courses_video'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    course_view_id = db.Column(None, db.ForeignKey('courses_view.id'), nullable=False)
    video_id = db.Column(None, db.ForeignKey('files.id'), nullable=False)

class BoughtCourses(db.Model):
    __tablename__ = 'bought_courses'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(None, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(None, db.ForeignKey('courses_view.id'), nullable=False)

class ExerciseView(db.Model):
    __tablename__ = 'exercises_view'

    class TYPE_EXERCISE:
        TEST = 1

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    type_exercise = db.Column(db.Integer())
    course_id = db.Column(None, db.ForeignKey('courses_view.id'), nullable=False)

class TestAnswer(db.Model):
    __tablename__ = 'test_answers'

    id = db.Column(db.Integer(), primary_key=True)
    text = db.Column(db.String())
    answer = db.Column(db.Boolean())
    exercise_view_id = db.Column(None, db.ForeignKey('exercises_view.id'), nullable=False)