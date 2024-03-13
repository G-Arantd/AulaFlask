from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import SECRET_KEY, DATABASE_URL

app: Flask = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db: SQLAlchemy = SQLAlchemy(app)

from app.Models import Tabelas

CORS(app, supports_credentials=True)

app.secret_key = SECRET_KEY

migrate: Migrate = Migrate(app, db)

from app.Routes import *