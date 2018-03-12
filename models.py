from marshmallow import Schema, fields, pre_load
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()


class AddUpdateDelete():   
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Customer(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name


class Project(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id', ondelete='CASCADE'), nullable=False)
    customer = db.relationship('Customer', backref=db.backref('projects', lazy='dynamic' , order_by='Project.name'))

    def __init__(self, name, customer):
        self.name = name
        self.customer = customer


class Task(db.Model, AddUpdateDelete):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id', ondelete='CASCADE'), nullable=False)
    project = db.relationship('Project', backref=db.backref('tasks', lazy='dynamic' , order_by='Task.name'))

    def __init__(self, name, project):
        self.name = name
        self.project = project


class CustomerSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    url = ma.URLFor('api.customerresource', id='<id>', _external=True)
    # projects = fields.Nested('ProjectSchema', many=True, exclude=('customer',))


class ProjectSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    url = ma.URLFor('api.projectresource', id='<id>', _external=True)
    customer = fields.Nested('CustomerSchema')
    # tasks = fields.Nested('TaskSchema', many=True, exclude=('project',))


class TaskSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(3))
    url = ma.URLFor('api.taskresource', id='<id>', _external=True)
