from gino import Gino 

db = Gino()

class User(db.Model):
    __tablename__ = 'users'

    class STATE_USER:
        Creatore = 1
        Client = 2

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    uuid = db.Column(db.String())
    active = db.Column(db.Boolean())
    second_name = db.Column(db.String(), nullable=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    img = db.Column(None, db.ForeignKey('files.id'), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    user_type = db.Column(db.Integer())
    data = db.Column(db.JSON()) # save bought courses

    @property
    def full_name(self):
        return '{} {}'.format(self.name self.second_name) if self.second_name else '{}'.format(self.name)

class Files(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer(), primary_key=True)
    url_img = db.Column(db.String())


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer(), primary_key=True)
    token = db.Column(db.String())
    expired = db.Column(db.Boolean())
