from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# initate a flask app
app = Flask(__name__)

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