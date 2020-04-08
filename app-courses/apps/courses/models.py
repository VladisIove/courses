from gino import Gino 

db = Gino()

class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column()

class Comment(db.Model):
    __tablename__ = 'comments'

