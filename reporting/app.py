import logging
import os
import sys
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_login import LoginManager
from utils import user_unauthorized_callback, load_user
from urls import add_urls

logging.basicConfig(level=logging.DEBUG)

# Determining the project root.
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

# Creating the Flask app object
app = Flask(__name__)

# Flask config settings
app.config['MONGODB_DB'] = 'ncdc'
app.config['SECRET_KEY'] = 'G7B8AjjCYb6W1wF8dLIrYTvjqGT2Mcqj0qspFzTb+T8m77YIkylufas3kinAXO8G'
app.debug = False

# Setting up the login manager for Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.unauthorized_handler(user_unauthorized_callback)
login_manager.user_loader(load_user)

# Setting up the connection to the MongoDB backend.
db = MongoEngine(app)

# Add all of the url rules for the application.  Any url answered by the application must be
# mapped to a view function here.
add_urls(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
