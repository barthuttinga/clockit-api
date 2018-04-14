from flask_marshmallow import Marshmallow

from .models import Customer, Project, Task

ma = Marshmallow()


class CustomerSchema(ma.ModelSchema):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'created_at', '_links']

    created_at = ma.DateTime(dump_only=True)
    _links = ma.Hyperlinks({
        'self': ma.URLFor('api.customers', id='<id>'),
        'collection': ma.URLFor('api.customers'),
        # 'projects': fields.Nested('ProjectSchema', many=True, exclude=('customer')),
    })


class ProjectSchema(ma.ModelSchema):
    class Meta:
        model = Project
        fields = ['id', 'name', 'created_at', 'customer']
        # fields = ['id', 'name', 'created_at', 'customer', '_links']

    created_at = ma.DateTime(dump_only=True)
    customer = ma.Nested(CustomerSchema, exclude=('projects'))
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('api.project', id='<id>', _external=True),
    #     'parent': ma.URLFor('api.projects'),
    # })

    # @pre_load()
    # def get_customer(self, data):
    #     if isinstance(data['customer'], int):
    #         data['customer'] = customer_service.find(data['customer']).__dict__
    #     return data


class TaskSchema(ma.ModelSchema):
    class Meta:
        model = Task
        fields = ['id', 'name', 'start', 'end', '_links']

    project = ma.Nested('ProjectSchema', exclude=('tasks'))
    # _links = ma.Hyperlinks({
    #     'self': ma.URLFor('api.task', id='<id>', _external=True),
    #     'parent': ma.URLFor('api.tasks'),
    # })


customer_schema = CustomerSchema()
project_schema = ProjectSchema()
task_schema = TaskSchema()
