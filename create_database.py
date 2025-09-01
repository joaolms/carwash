from carwash import database, app
from carwash.models import User, Vehicle, Booking

# Create database carwash.db
with app.app_context():
    database.create_all()
