from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
db = SQLAlchemy(app)



app.config['SECRET_KEY'] = 'supersecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'btw17.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

app.config.from_object(__name__)







