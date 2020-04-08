from gino import Gino 

db = Gino()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    second_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String)
    img = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=True)
    age = db.Column(db.Integer, nullable=True)

    @property
    def full_name(self):
        return '{} {}'.format(self.name self.second_name) if self.second_name else '{}'.format(self.name)

class Files(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True)
    url_img = db.Column(db.String)


