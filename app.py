import os
from flask import Flask
from flask_migrate import Migrate
from models.model import *
from models.connection import db
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
    