from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Length, ValidationError



class RegistrationForm(FlaskForm):

	username = wtforms.StringField("Username", [DataRequired(), Length(min=3, max=20)])
	password = wtforms.PasswordField("Password", [DataRequired(), Length(min=8)])
	confirm_password = wtforms.PasswordField("confirm Password", [DataRequired()])

	submit_button = wtforms.SubmitField("Sign Up")

	# def validate_confirm_password(self, confirm_password):

	# 	if confirm_password != self.password: search how to get fields inside another field validation
	# 		raise ValidationError("passswords don't match")


class LoginForm(FlaskForm):
	username = wtforms.StringField("Username", [DataRequired()])
	password = wtforms.PasswordField("Password", [DataRequired()])

	submit_button = wtforms.SubmitField("Login")