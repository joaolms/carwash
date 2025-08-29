from carwash import app
from flask import render_template, url_for
from flask_login import login_required
from carwash.forms import FormLogin, FormNewUser


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.route('/', methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("main.html", form=formlogin)


@app.route('/user/new', methods=["GET", "POST"])
def new_user():
    formnewuser = FormNewUser()
    return render_template("user_new.html", form=formnewuser)


@app.route('/booking')
# @login_required
def booking():
    return 'booking services'


@app.route('/booking/new')
@login_required
def schedules_new():
    return 'Booking a new service'


@app.route('/customers')
# @login_required
def customers():
    return 'Customers list'


@app.route('/customers/new')
@login_required
def customers_new():
    return 'Add a new customer'


@app.route('/vehicles')
# @login_required
def vehicles():
    return 'Vehicles list'


@app.route('/vehicles/new')
@login_required
def vehicles_new():
    return 'Add a new vehicle'


@app.route('/services')
# @login_required
def services():
    return 'Services list'


@app.route('/services/new')
@login_required
def services_new():
    return 'Add a new services'