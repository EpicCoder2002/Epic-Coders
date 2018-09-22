from EpicCoders import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from EpicCoders.forms import RegistrationForm, LoginForm
from EpicCoders.models import User
from flask_login import current_user, login_user, logout_user




@app.route('/')
def Home(): 

	return render_template("Home.html")


@app.route('/register', methods=["GET", "POST"])
def register(): 
	form = RegistrationForm()
	if form.validate_on_submit():
		password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
		user = User(username=form.username.data, password=password)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for("Home"))
	return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
	if current_user.is_authenticated:
		redirect(url_for("Home"))

	login_form = LoginForm()

	if login_form.validate_on_submit():
		user = User.query.filter_by(username=login_form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, login_form.password.data):
			login_user(user, remember=False)
			next_page = request.args.get("next") # next is set on login_required views

			return redirect(url_for(next_page)) if next_page else redirect(url_for("Home"))
		else:
			redirect(url_for("Home"))

	return render_template("login.html", form=login_form)


@app.route('/logut', methods=["GET", "POST"])
def logout():
	logout_user()
	return render_template("Home.html")


# @app.route('/account')
# @login_required
# def account():

# 	return render_template("account.html")