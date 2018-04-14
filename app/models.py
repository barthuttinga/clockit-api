from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    team_id = db.Column(db.Integer,
                        db.ForeignKey('team.id', ondelete='CASCADE'),
                        nullable=True)
    team = db.relationship(Team, backref=db.backref('users',
                                                    lazy='dynamic',
                                                    order_by='User.username'))

    # @property
    # def get_password(self):

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    team_id = db.Column(db.Integer,
                        db.ForeignKey('team.id', ondelete='CASCADE'),
                        nullable=False)
    team = db.relationship(Team, backref=db.backref('customers',
                                                    lazy='dynamic',
                                                    order_by='Customer.name'))


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    customer_id = db.Column(db.Integer,
                            db.ForeignKey('customer.id', ondelete='CASCADE'),
                            nullable=False)
    customer = db.relationship('Customer', backref=db.backref('projects',
                                                              lazy='dynamic',
                                                              order_by='Project.name'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=True)
    user = db.relationship(User, backref=db.backref('projects',
                                                    lazy='dynamic',
                                                    order_by='Project.name'))


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=True)
    project_id = db.Column(db.Integer,
                           db.ForeignKey('project.id', ondelete='CASCADE'),
                           nullable=False)
    project = db.relationship('Project',
                              backref=db.backref('tasks', lazy='dynamic',
                                                 order_by='Task.name'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('user.id', ondelete='CASCADE'),
                        nullable=True)
    user = db.relationship(User, backref=db.backref('tasks',
                                                    lazy='dynamic',
                                                    order_by='Task.name'))
