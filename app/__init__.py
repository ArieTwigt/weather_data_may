from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

from dotenv import load_dotenv

# load the env file
load_dotenv()

# initate a flask app
app = Flask(__name__)

# add the secret key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# specify the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

# initiate the database
db = SQLAlchemy() 

# initate the app
db.init_app(app)


# initate the database for the app
migrate = Migrate(app, db)

# import the models and routes
from . import routes, models