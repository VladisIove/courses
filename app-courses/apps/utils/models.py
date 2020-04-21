from gino.ext.aiohttp import Gino

db = Gino()

class FAQ(db.Model):
    __tablename__ = 'faqs'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)