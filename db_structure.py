import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import exc
from flask_login import LoginManager, UserMixin
from user_model import *
from werkzeug.security import generate_password_hash, check_password_hash



DEBUG_DATABASE = True


project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "task_database.db"))
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



 #############################################################
###############################################################
##                                                           ##
##                     DATABASE CODE                         ##
##                                                           ##
###############################################################
 #############################################################


class VarianTaskTemplate(db.Model):
	__tablename__ = "variant_task"
	id 				= db.Column(db.Integer, primary_key=True)
	topic 			= db.Column(db.String(80), unique=False,  nullable=False, primary_key=False)
	diff 			= db.Column(db.Integer, unique=False,  nullable=False, primary_key=False)
	variables 		= db.Column(db.String(120), unique=False,  nullable=False, primary_key=False)
	is_graph 		= db.Column(db.Boolean, unique=False, nullable=False, primary_key=False)
	grahp_template 	= db.Column(db.String(240), unique=False, nullable=True, primary_key=False)
	task_template 	= db.Column(db.String(240), unique=True,  nullable=False, primary_key=False)
	sol_template 	= db.Column(db.String(240), unique=False,  nullable=False, primary_key=False)
	is_variant		= db.Column(db.Boolean, unique=False, nullable=False, primary_key=False)
	num_solutions 	= db.Column(db.Integer, unique=False,  nullable=False, primary_key=False)

	def __repr__(self):
		return "id : {} | topic : | {} task_template : {} | sol_template : {}".format(self.id, self.topic, self.task_template, self.sol_template)



class User(UserMixin, db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	answers = relationship("Answer", back_populates = "attached_user")

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)


class Answer(db.Model):
	__tablename__ = "task_answer"
	id 			  = db.Column(db.Integer, primary_key=True)
	user_id       = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	seed 		  = db.Column(db.Integer, unique=False,  nullable=False, primary_key=False)
	answers_str   = db.Column(db.String(500), unique=False, nullable=False, primary_key=False)
	attached_user = relationship("User", back_populates="answers")

	def __repr__(self):
		return "id : {} | user_id : | {} seed : {} | answers_str : {}".format(self.id, self.user_id, self.seed, self.answers_str)




db.create_all()
