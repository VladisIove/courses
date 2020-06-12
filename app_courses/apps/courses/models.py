from apps.init_db import db


class CourseView(db.Model):
    __tablename__ = 'courses_view'

    id = db.Column(db.Integer(), primary_key=True)
    name_course = db.Column(db.String())
    description = db.Column(db.String())
    author_id = db.Column(None, db.ForeignKey('users.id'), nullable=True)
    date = db.Column(db.DateTime())
    price = db.Column(db.Integer())
    old_price = db.Column(db.Integer())
    data = db.Column(db.JSON())

    key_dict = ['name_course', 'description', 'author_id', 'date', 'price', 'old_price', 'data']

class CourseVideo(db.Model):
    __tablename__ = 'courses_video'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    course_view = db.Column(None, db.ForeignKey('courses_view.id'), nullable=False)
    video = db.Column(None, db.ForeignKey('files.id'), nullable=False)

