import uuid 
import hashlib
import binascii
import os
 
from apps.init_db import db

class User(db.Model):
    __tablename__ = 'users'

    class STATE_USER:
        Admin = 1
        Creatore = 2
        Support = 3 
        Client = 4
        

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    uuid = db.Column(db.String(), default=uuid.uuid1())
    active = db.Column(db.Boolean())
    second_name = db.Column(db.String(), nullable=True)
    email = db.Column(db.String())
    password = db.Column(db.String())
    img_id = db.Column(None, db.ForeignKey('files.id'), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    user_type = db.Column(db.Integer())
    data = db.Column(db.JSON())

    @property
    def full_name(self):
        return '{} {}'.format(self.name, self.second_name) if self.second_name else '{}'.format(self.name)

    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
 
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.String())

    def save_file(self, file, file_format):
        pass


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(None, db.ForeignKey('users.id'), nullable=True)
    token = db.Column(db.String(), default=uuid.uuid1())
    expired = db.Column(db.Boolean())
