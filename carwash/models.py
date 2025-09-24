from carwash import database, login_manager
from datetime import datetime, timezone

# UserMixin tell to the app which class is management the login process
from flask_login import UserMixin


# Fetch the user from database by ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String, nullable=False)
    username = database.Column(database.String(80), nullable=False, unique=True)
    password = database.Column(database.String(120), nullable=False)
    phone = database.Column(database.String(20), nullable=False)
    role = database.Column(database.String(15), nullable=False, default='User')
    image = database.Column(database.String, default='user_default.png')
    vehicles = database.relationship('Vehicle', backref='owner', lazy=True)


class Vehicle(database.Model):
    plate = database.Column(database.String(10), primary_key=True, unique=True, nullable=False)
    model = database.Column(database.String(30), nullable=False)
    year = database.Column(database.Integer)
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)


class Booking(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    create_at = database.Column(database.DateTime, nullable=False, default=datetime.now(timezone.utc))
    appointment = database.Column(database.DateTime, nullable=False)
    vehicle = database.relationship('Vehicle', backref='booking', lazy=True)
    status = database.Column(database.String(20), default='Booked')


class Service(database.Model):
    id = database.Column(database.Integer, primary_key=True, unique=True, nullable=False)
    service = database.Column(database.String(30), nullable=False)
    cost = database.Column(database.Float, nullable=False)