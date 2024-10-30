from models.connection import db
from flask_bcrypt import Bcrypt 
from flask_login import UserMixin

bcrypt = Bcrypt() 

class QrData(db.Model):
    id = db.Column(db.Integer,unique=True, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    link = db.Column(db.String(120), unique=False, nullable=False)
    color = db.Column(db.String(10), unique=False, nullable=False)
    back = db.Column(db.String(10), unique=False, nullable=False)
    filename = db.Column(db.String(120), unique=False, nullable=False)


class QrUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128)) 

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash (password).decode('utf-8') 

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'