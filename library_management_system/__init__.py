from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from . import models
from .admin_routes import admin_bp
from .user_routes import user_bp

app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)
