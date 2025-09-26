from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)

# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///carwash.db"
database = SQLAlchemy(app)

# Login
## SECRET_KEY will be used in the CSRF forms and for encrypt the user password
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
## If not logged in, the user will be redirected to the homepage
login_manager.login_view = 'login'


from carwash import routes
