from carwash import app, database, bcrypt
from carwash.models import User
from flask import render_template, url_for, redirect, flash
from flask_login import login_required, login_user, logout_user, current_user
from carwash.forms import FormLogin, FormNewUser


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/', methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()

    # Check if login form is valid
    if formlogin.validate_on_submit():
        # Get user info from database
        user = User.query.filter_by(username=formlogin.username.data).first()

        # If user exist and the password is correct, logging user is accepted.
        ## Compare the hash using bcrypt from password stored in database
        ## and the password entered in the login form
        if user and bcrypt.check_password_hash(user.password, formlogin.password.data):
            login_user(user, remember=True)
            return redirect(url_for("users"))
    else:
        flash('Incorrect password or username')

    return render_template("main.html", form=formlogin)


@app.route('/users/new', methods=["GET", "POST"])
def new_user():
    formnewuser = FormNewUser()

    # Did the user click the submit button on the form and is the data valid?
    # Then we will create a new user account
    if formnewuser.validate_on_submit():
        # Encrypt the user password with Bcrypt
        # Bcrypt will use the SECRET_KEY env variable to encrypt
        password_encrypted = bcrypt.generate_password_hash(formnewuser.password.data)

        user = User(name=formnewuser.name.data,
                    username=formnewuser.username.data,
                    password=password_encrypted,
                    phone=formnewuser.phone_number.data)

        # Add the user to the database
        database.session.add(user)
        database.session.commit()

        # After to create a new account, the user should be
        # logged in (login_user()) and redirect to a new page, in this case
        # the user will be redirect to the USERS page, where
        # "user" is a function of the routes.py.
        login_user(user, remember=True)
        return redirect(url_for("users"))

    return render_template("users/new.html", form=formnewuser)


@app.route('/users')
@login_required
# @login_required
def users():
    return render_template('/users/list.html')


@app.route('/booking')
@login_required
# @login_required
def booking():
    return render_template('booking/list.html')


@app.route('/booking/new')
@login_required
def schedules_new():
    return 'Booking a new service'


@app.route('/vehicles')
@login_required
# @login_required
def vehicles():
    return render_template('vehicles/list.html')


@app.route('/vehicles/new')
@login_required
def vehicles_new():
    return 'Add a new vehicle'


@app.route('/services')
@login_required
# @login_required
def services():
    return render_template('services/list.html')


@app.route('/services/new')
@login_required
def services_new():
    return 'Add a new services'
