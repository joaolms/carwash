from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError
from carwash.models import User


class FormLogin(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirmation_button = SubmitField("Login")


class FormNewUser(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired(), Length(3, 12)])
    password = PasswordField("Password", validators=[DataRequired(), Length(6, 20)])
    password_confirmation = PasswordField("Password confirmation", validators=[DataRequired(), EqualTo("password", message="Passwords must match")])
    phone_number = StringField("Phone number")
    confirmation_button = SubmitField("Create")

    # Validate if username is unique
    # The name of this function HAVE TO be VALIDATE_ + FIELD_NAME.
    # It will be used by validate_on_submit function on the routes
    # this function will be executed automatically with validate_on_submit()
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            return ValidationError("Username already exists.")
