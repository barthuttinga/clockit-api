from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from models import db, Customer, CustomerSchema, Project, ProjectSchema, Task, TaskSchema
from sqlalchemy.exc import SQLAlchemyError
import status


api_bp = Blueprint('api', __name__)
customer_schema = CustomerSchema()
project_schema = ProjectSchema()
task_schema = TaskSchema()
api = Api(api_bp)


class CustomerResource(Resource):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        result = customer_schema.dump(customer).data
        return result


class ProjectResource(Resource):
    def get(self, id):
        project = Project.query.get_or_404(id)
        result = project_schema.dump(project).data
        return result


class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id)
        result = task_schema.dump(taks).data
        return result


class CustomerListResource(Resource):
    def get(self):
        customers = Customer.query.all()
        result = customer_schema.dump(customers, many=True).data
        return result


class CustomerProjectListResource(Resource):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        projects = customer.query.all()
        # projects = Project.query.all()
        result = project_schema.dump(projects, many=True).data
        return result


class ProjectListResource(Resource):
    def get(self):
        projects = Project.query.all()
        result = project_schema.dump(projects, many=True).data
        return result


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        result = task_schema.dump(tasks, many=True).data
        return result


api.add_resource(CustomerListResource, '/customers/')
api.add_resource(CustomerResource, '/customers/<int:id>')
api.add_resource(CustomerProjectListResource, '/customers/<int:id>/projects/')
api.add_resource(ProjectListResource, '/projects/')
api.add_resource(ProjectResource, '/projects/<int:id>')
api.add_resource(TaskListResource, '/tasks/')
api.add_resource(TaskResource, '/tasks/<int:id>')
