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


@app.route('/user')
# @login_required
def users():
    return render_template('user/list.html')


@app.route('/user/new', methods=["GET", "POST"])
def new_user():
    formnewuser = FormNewUser()
    return render_template("user_new.html", form=formnewuser)


@app.route('/booking')
# @login_required
def booking():
    return render_template('booking/list.html')


@app.route('/booking/new')
@login_required
def schedules_new():
    return 'Booking a new service'


@app.route('/vehicles')
# @login_required
def vehicles():
    return render_template('vehicle/list.html')


@app.route('/vehicles/new')
@login_required
def vehicles_new():
    return 'Add a new vehicle'


@app.route('/services')
# @login_required
def services():
    return render_template('service/list.html')


@app.route('/services/new')
@login_required
def services_new():
    return 'Add a new services'
