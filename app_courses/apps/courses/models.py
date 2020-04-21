from apps.init_db import db


class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer(), primary_key=True)
    name_course = db.Column(db.String())
    description = db.Column(db.String())
    author = db.Column(None, db.ForeignKey('users.id'), nullable=True)
    date = db.Column(db.DateTime())
    price = db.Column(db.Integer())
    old_price = db.Column(db.Integer())
    data_json = db.Column(db.JSON()) # save id videos, files and img