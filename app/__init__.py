from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project2:project2@localhost/project2"
db = SQLAlchemy(app)


from app import views
db.create_all()