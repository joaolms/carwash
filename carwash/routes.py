from carwash import app
from flask import render_template, url_for


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.route('/')
def homepage():
    return render_template("main.html")


@app.route('/login')
def login():
    return 'Login page'


@app.route('/booking')
def booking():
    return 'booking services'


@app.route('/booking/new')
def schedules_new():
    return 'Booking a new service'


@app.route('/customers')
def customers():
    return 'Customers list'


@app.route('/customers/new')
def customers_new():
    return 'Add a new customer'


@app.route('/vehicles')
def vehicles():
    return 'Vehicles list'


@app.route('/vehicles/new')
def vehicles_new():
    return 'Add a new vehicle'


@app.route('/services')
def services():
    return 'Services list'


@app.route('/services/new')
def services_new():
    return 'Add a new services'