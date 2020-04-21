from apps.init_db import db

class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)