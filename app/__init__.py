
from flask import Flask  # import Flask



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:alif19090068@localhost/flask_crud'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
from app.controllers import *

