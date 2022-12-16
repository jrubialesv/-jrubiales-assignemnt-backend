from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
# Select environment based on the ENV environment variabled
if os.getenv('ENV') != 'dev':
    print("Running in production mode")
    app.config.from_object('config.ProductionConfig')
else:
    print("Running in development mode")
    app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)

from recipes_api.models import Recipes
from recipes_api import routes

db.create_all()
CORS(app)
