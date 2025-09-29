from carwash import app, database, bcrypt
from carwash.models import User, Vehicle, Booking, Service
from flask import render_template, url_for, redirect, flash,request
from flask_login import login_required, login_user, logout_user, current_user
from carwash.forms import FormLogin, FormNewUser, FormNewVehicle, FormNewBooking, FormNewService, FormEditUser, FormVehicleEdit, FormServiceEdit
from datetime import datetime\


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404


@app.route('/', methods=["GET"])
def homepage():
    return render_template("main.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))


@app.route('/login', methods=["GET", "POST"])
def login():
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
            return redirect(url_for("homepage"))
        else:
            flash('Incorrect password or username', 'error')

    return render_template("auth/login.html", form=formlogin)


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
                    role=formnewuser.role.data,
                    phone=formnewuser.phone_number.data)

        # Add the user to the database
        database.session.add(user)
        database.session.commit()

        # After to create a new account, the user should be
        # logged in (login_user()) and redirect to a new page, in this case
        # the user will be redirected to the USERS page, where
        # "user" is a function of the routes.py.
        login_user(user, remember=True)
        return redirect(url_for("users"))

    return render_template("users/new.html", form=formnewuser)


@app.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('/users/list.html', users=users)

@app.route('/vehicles')
@login_required
def vehicles():
    vehicles = Vehicle.query.all()
    return render_template('vehicles/list.html', vehicles=vehicles)


@app.route('/<int:user_id>/edit_user', methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    current_user_info = User.query.filter_by(id=user_id).first()
    form = FormEditUser()

    if form.validate_on_submit():
        if form.password.data:
            password_encrypted = bcrypt.generate_password_hash(form.password.data)
        else:
            password_encrypted = current_user_info.password

        # Update user register
        User.query.filter_by(id=user_id).update({
            "name": form.name.data,
            "phone": form.phone_number.data,
            "role": form.role.data,
            "password": password_encrypted
        })
        database.session.commit()

        return redirect(url_for("users"))

    return render_template("users/edit.html", user=current_user_info, form=form)

@app.route('/<int:user_id>/delete', methods=["GET", "POST", "PUT"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    database.session.delete(user)
    database.session.commit()
    return redirect(url_for("users"))


@app.route('/vehicles/new', methods=["GET", "POST"])
@login_required
def vehicles_new():
    owners = User.query.all()
    formnewvehicle = FormNewVehicle()

    if formnewvehicle.validate_on_submit():

        vehicle = Vehicle(
            plate = formnewvehicle.plate.data,
            model = formnewvehicle.model.data,
            year = formnewvehicle.year.data,
            user_id = formnewvehicle.owner.data,
        )

        database.session.add(vehicle)
        database.session.commit()

        return redirect(url_for("vehicles"))

    return render_template('vehicles/new.html', form=formnewvehicle, owners=owners)


@app.route('/vehicles/<vehicle_plate>/edit', methods=["GET", "POST"])
@login_required
def vehicle_edit(vehicle_plate):
    vehicle = Vehicle.query.get(vehicle_plate)
    owners = User.query.all()
    form = FormVehicleEdit()

    if form.validate_on_submit():
        Vehicle.query.filter_by(plate=vehicle_plate).update({
            "user_id": form.owner.data,
            "model": form.model.data
        })
        database.session.commit()
        return redirect(url_for("vehicles"))

    return render_template("vehicles/edit.html", vehicle=vehicle, form=form, owners=owners)


@app.route('/vehicles/<vehicle_plate>/delete', methods=["GET", "POST"])
@login_required
def vehicle_delete(vehicle_plate):
    vehicle = Vehicle.query.get(vehicle_plate)
    database.session.delete(vehicle)
    database.session.commit()
    return redirect(url_for("vehicles"))


@app.route('/booking')
@login_required
def booking():
    bookings = Booking.query.all()
    return render_template('booking/list.html', bookings=bookings)


@app.route('/booking/new', methods=["GET", "POST"])
@login_required
def schedules_new():
    formnewbooking = FormNewBooking()
    vehicles = Vehicle.query.all()
    services = Service.query.all()

    # Dynamic choices for SelectField on the form
    formnewbooking.vehicle_plate.choices = [(v.plate, f'{v.plate} - {v.model}, de {v.owner.name}') for v in vehicles]
    formnewbooking.service_id.choices = [(s.id, s.service) for s in services]

    if formnewbooking.validate_on_submit():
        print(f'Validated on submit\nPlate: {formnewbooking.vehicle_plate.data}')
        booking = Booking(
            vehicle_plate = formnewbooking.vehicle_plate.data,
            service_id = formnewbooking.service_id.data
        )

        database.session.add(booking)
        database.session.commit()
        print(f'Booking saved: {booking}')

        return redirect(url_for("booking"))
    else:
        print(f'failed to validate booking form\nPlate: {formnewbooking.vehicle_plate.data}\nService_id: {formnewbooking.service_id.data}')
        print(f'Form errors: {formnewbooking.errors}')

    return render_template('booking/new.html', form=formnewbooking, vehicles=vehicles, services=services)


@app.route('/services')
@login_required
def services():
    services = Service.query.all()
    return render_template('services/list.html', services=services)


@app.route('/services/new', methods=["GET", "POST"])
@login_required
def services_new():
    formnewservice = FormNewService()

    if formnewservice.validate_on_submit():

        service = Service(
            service = formnewservice.service.data,
            cost = formnewservice.cost.data
        )

        database.session.add(service)
        database.session.commit()
        return redirect(url_for("services"))

    return render_template('services/new.html', form=formnewservice)


@app.route('/services/<int:id>/edit', methods=["GET", "POST"])
@login_required
def service_edit(id):
    service = Service.query.get(id)
    form = FormServiceEdit()

    if form.validate_on_submit():
        Service.query.filter_by(id=id).update({
            "service": form.service.data,
            "cost": form.cost.data
        })
        database.session.commit()
        return redirect(url_for("services"))

    return render_template("services/edit.html", form=form, service=service)


@app.route('/services/<int:id>/delete', methods=["GET", "POST"])
@login_required
def service_delete(id):
    service = Service.query.get(id)
    database.session.delete(service)
    database.session.commit()
    return redirect(url_for("services"))