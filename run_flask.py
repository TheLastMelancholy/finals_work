from db_structure import *
from generator import *
from flask import Flask, request, render_template, url_for, session, redirect, flash
import random
import os
import calendar
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash
#from werkzeug.ImmutableMultiDict import iteritems
from flask_login import LoginManager, UserMixin
from flask_wtf import FlaskForm
from flask_login import login_required, current_user, login_user, logout_user

from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import email_validator


#app = Flask(__name__)
login_mnager = LoginManager()
login_mnager.init_app(app)
login_mnager.login_view = 'login_repr'

 #############################################################
###############################################################
##                                                           ##
##                        AUTH MODEL                         ##
##                                                           ##
###############################################################
 #############################################################


@login_mnager.user_loader
def load_user(id):
	return User.query.get(int(id))


class LoginForm(FlaskForm):
	username = StringField('Username')
	password = PasswordField('Password')
	submit = SubmitField('Submit')


@app.route('/login', methods=['GET', 'POST'])
def login_repr():
	if current_user.is_authenticated:
		return redirect(url_for('homepage'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')
			return redirect(url_for('login_repr'))
		login_user(user)
		return redirect(url_for('generate_test'))
	return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('generate_test'))



class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('generate_test'))
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(username=form.username.data, email=form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Congratulations, you are now a registered user!')
		return redirect(url_for('login_repr'))
	return render_template('register.html', title='Register', form=form)





 #############################################################
###############################################################
##                                                           ##
##                        TEST MODEL                         ##
##                                                           ##
###############################################################
 #############################################################





tasks = []

@app.route("/random_test")
def generate_test():
	global tasks
	#if seed is None:

	seed  = random.randint(10**10,10**15)
	random.seed(seed)
	return redirect(url_for("generate_test_seeded", seed=seed))
	#tasks = generate_tasks(["Числа и выражения"],[1],[1],[1],18,0)
	#else:
	#tasks = generate_tasks(["Числа и выражения"],[1],[1],[1],18,0, seed=seed)
	#return render_template("generated_test.html", a_tasks=tasks, answers_url='show_answers', new_task_url='generate_test', seed=seed)

@app.route("/random_test/<seed>")
def generate_test_seeded(seed):
	print("called with seed of ", seed)
	global tasks
	#if seed is None:
	tasks = generate_tasks(["Числа и выражения"],[1],[1],[1],18,0, seed=seed)
	#else:
	#tasks = generate_tasks(["Числа и выражения"],[1],[1],[1],18,0, seed=seed)
	return render_template("generated_test.html", a_tasks=tasks, answers_url='show_answers', new_task_url='generate_test', seed=seed)



@app.route("/test", methods=["GET", "POST"])
def test_task():
	if request.method=="GET":
		return render_template("test_task.html")
	if request.method=="POST":
		return render_template("test_task.html")

@app.route("/upload", methods=["GET", "POST"])
def upload_task():
	if request.method=='POST':
		#ADD TASK TO DB
		#return redirect(url_for("test_task"))
		return render_template("template_tester.html")
	if request.method=='GET':
		#return redirect(url_for("test_task"))
		return render_template("template_tester.html")

@app.route("/answers/<seed>", methods=["POST", "GET"])
def show_answers(seed):
	def parse_answers_str(answers_str):
		return [int(_) for _ in answers_str[:-1].split(",")]
	tasks = generate_tasks(["Числа и выражения"],[1],[1],[1],18,0, seed=seed)
	if request.method=='POST':
		answers=[]
		print(request.form)
		answers_str = ""
		for i in range(1,40):
			if str(i) in request.form:
				answers.append(int(request.form[str(i)]))
				answers_str+="{},".format(request.form[str(i)])
			else:
				answers.append(0)
				answers_str+="{},".format(0)
		#print(answers_str)
		#answers.append(int(request.form[answer]))
		#print(answers)
		if(current_user.is_authenticated):
			answer = Answer(user_id=current_user.id, seed=seed, answers_str=answers_str)
			print(answer)
			db.session.add(answer)
			db.session.commit()


		return render_template("show_answers.html", a_tasks=tasks, new_task_url='generate_test', seed=seed, answers=answers)
	if request.method=='GET':
		if(not current_user.is_authenticated):
			redirect(url_for("homepage"))
		else:
			answers_str=""
			for a in current_user.answers:
				print("###############################")
				print(a)
				print(seed)
				print(a.seed)
				print(int(seed)==a.seed)
				print(seed.__class__)
				print(a.seed.__class__)
				if(a.seed==int(seed)):
					answers_str=a.answers_str
					break

		#answers_str="3,0,0,0,0,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"
			return render_template("show_answers.html", a_tasks=tasks, new_task_url='generate_test', seed=seed, answers=parse_answers_str(answers_str))

@app.route("/index")
def homepage():
	completed_tests = []
	if(current_user.is_authenticated):
		for a in current_user.answers:
			completed_tests.append(a.seed)
	return render_template("index.html", new_task_url = 'generate_test', is_authenticated = current_user.is_authenticated, completed_tests = completed_tests, answers_url='show_answers')



if __name__ == '__main__':
	app.secret_key = 'test app secret key'
	app.run(host='127.0.0.1')