from flask import Flask
import os

from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

ma = Marshmallow(app)



app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'btw17.db')
db = SQLAlchemy(app)

from app import models, views

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app.config.from_object(__name__)







