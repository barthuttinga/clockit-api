import json

from app.models import Customer, Project, Task
from app.schemas import customer_schema, project_schema, task_schema
from . import AppTestCase


class TestCase(AppTestCase):
    def test_deserialize_customer(self):
        customer, errors = customer_schema.loads(json.dumps({
            'name': 'Some customer',
        }))

        assert 0 == len(errors)
        assert type(customer) == Customer
        assert customer.name == 'Some customer'

    def test_deserialize_project(self):
        project, errors = project_schema.loads(json.dumps({
            'name': 'Some project',
            'customer': {
                'id': 1,
                'name': 'Some customer',
            },
        }))

        assert 0 == len(errors)
        assert type(project) == Project
        assert project.name == 'Some project'

    def test_deserialize_task_without_end_time(self):
        data = {
            'name': 'Some task',
            'start': '2018-03-26 10:00:00+02:00',
        }
        task, errors = task_schema.loads(json.dumps(data))

        assert 0 == len(errors)
        assert type(task) == Task
        assert task.name == 'Some task'
        assert str(task.start) == '2018-03-26 10:00:00+02:00'
        assert task.end == None

    def test_deserialize_task_with_end_time(self):
        data = {
            'name': 'Some task',
            'start': '2018-03-26T10:00:00',
            'end': '2018-03-26T15:30',
        }
        task, errors = task_schema.loads(json.dumps(data))

        assert 0 == len(errors)
        assert type(task) == Task
        assert task.name == 'Some task'
        assert str(task.start) == '2018-03-26 10:00:00'
        assert str(task.end) == '2018-03-26 15:30:00'
