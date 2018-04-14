from flask import Blueprint, request
from flask_cors import CORS
from flask_jwt import jwt_required
from flask_restful import Api, Resource

from .models import Customer, Project, Task
from .schemas import customer_schema, project_schema, task_schema
from .services import customer_service, project_service
from .status import *

api_bp = Blueprint('api', __name__)
CORS(api_bp)


class CustomerListResource(Resource):
    decorators = [jwt_required()]

    def get(self):
        customers = customer_service.findAll()
        return customer_schema.dump(customers, many=True).data

    def post(self):
        customer, errors = customer_schema.load(request.json)
        if errors:
            return errors, HTTP_400_BAD_REQUEST
            customer_service.add(customer)
        return customer_schema.dump(customer).data, HTTP_201_CREATED


class CustomerResource(Resource):
    def get(self, id):
        customer = customer_service.find(id)
        return customer_schema.dump(customer).data

    def put(self, id):
        customer = customer_service.find(id)
        # todo: update
        customer_service.update(customer)
        return customer_schema.dump(customer).data

    def delete(self, id):
        customer = customer_service.find(id)
        customer_service.delete(customer)
        return '', HTTP_204_NO_CONTENT


class ProjectListResource(Resource):
    def get(self):
        projects = Project.query.all()
        return project_schema.dump(projects, many=True).data

    def post(self):
        project, errors = project_schema.load(request.json)
        if errors:
            return errors, HTTP_400_BAD_REQUEST
        project_service.add(project)
        return project_schema.dump(project).data, HTTP_201_CREATED


class ProjectResource(Resource):
    def get(self, id):
        project = Project.query.get_or_404(id)
        result = project_schema.dump(project).data
        return result

    def put(self, id):
        customer = customer_service.find(id)
        # args = customer_parser.parse_args()
        customer.name = args['name']
        customer_service.update(customer)
        return customer_schema.dump(customer).data

    def delete(self, id):
        customer = customer_service.find(id)
        customer_service.delete(customer)
        return '', HTTP_204_NO_CONTENT


class CustomerProjectListResource(Resource):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        projects = customer.query.all()
        # projects = Project.query.all()
        result = project_schema.dump(projects, many=True).data
        return result

    def post(self, id):
        customer = Customer.query.get_or_404(id)
        project, errors = project_schema.load(request.json)
        if errors:
            return errors, HTTP_400_BAD_REQUEST
        project.customer = customer
        project_service.add(project)
        return project_schema.dump(project).data, HTTP_201_CREATED


class ProjectTaskListResource(Resource):
    def get(self, id):
        customer = Customer.query.get_or_404(id)
        projects = customer.query.all()
        # projects = Project.query.all()
        result = project_schema.dump(projects, many=True).data
        return result

    def post(self, id):
        customer = Customer.query.get_or_404(id)
        project, errors = project_schema.load(request.json)
        if errors:
            return errors, HTTP_400_BAD_REQUEST
        project.customer = customer
        project_service.add(project)
        return project_schema.dump(project).data, HTTP_201_CREATED


class TaskResource(Resource):
    def get(self, id):
        task = Task.query.get_or_404(id)
        result = task_schema.dump(task).data
        return result


class TaskListResource(Resource):
    def get(self):
        tasks = Task.query.all()
        result = task_schema.dump(tasks, many=True).data
        return result


api = Api(api_bp)
api.add_resource(CustomerListResource, '/customers/', endpoint='customers')
api.add_resource(CustomerResource, '/customers/<int:id>', endpoint='customer')
api.add_resource(CustomerProjectListResource, '/customers/<int:id>/projects/',
                 endpoint='customer_projects')
api.add_resource(ProjectListResource, '/projects/', endpoint='projects')
api.add_resource(ProjectResource, '/projects/<int:id>', endpoint='project')
api.add_resource(ProjectTaskListResource, '/project/<int:id>/tasks/',
                 endpoint='project_tasks')
api.add_resource(TaskListResource, '/tasks/', endpoint='tasks')
api.add_resource(TaskResource, '/tasks/<int:id>', endpoint='task')
