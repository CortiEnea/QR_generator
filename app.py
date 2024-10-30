import os
from flask import Flask, redirect, request, url_for 
from flask_migrate import Migrate
from models.model import *
from models.connection import db
from dotenv import load_dotenv
from flask_qrcode import QRcode
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from routes.auth import auth as bp_auth
from routes.qr import qrcode as bp_qr
from flask_login import LoginManager


app = Flask(__name__)
app.register_blueprint(bp_auth, url_prefix='/')
app.register_blueprint(bp_qr, url_prefix='/QR')
load_dotenv()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['UPLOAD_FOLDER'] = 'static/'

db.init_app(app)

migrate = Migrate(app, db)
QRcode(app)

class ProtectedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('auth.login', next=request.url))
    
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    stmt = db.select(QrUser).filter_by(id=user_id)
    user = db.session.execute(stmt).scalar_one_or_none()
    return user

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
