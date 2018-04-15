import json
import unittest

from faker import Faker
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

from config_test import ConfigTest
from .. import create_app
from ..models import Customer, Project, Task, Team, User

app = create_app(ConfigTest)


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()
        self.app_context = app.test_request_context()
        self.app_context.push()

        from ..models import db
        db.create_all()
        self.load_fixtures(db)

    def tearDown(self):
        from ..models import db
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def load_fixtures(self, db: SQLAlchemy):
        fake = Faker('nl_NL')
        fake.seed(1)

        self.team = Team(name='Joe\'s team')
        db.session.add(self.team)

        user = User(username='joe', team=self.team)
        user.set_password('pass')
        db.session.add(user)

        for i in range(4):
            customer = Customer(name=fake.company(), team=self.team)
            db.session.add(customer)
            for j in range(3):
                project = Project(name=fake.word(), customer=customer)
                db.session.add(project)
                for k in range(2):
                    task = Task(name=fake.sentence(),
                                start=fake.date_time_this_decade(),
                                project=project)
                    db.session.add(task)
        db.session.commit()

    def get_token(self, username, password):
        url = url_for('_default_auth_request_handler', _external=True)
        headers = {'Content-Type': 'application/json'}
        data = {
            'username': username,
            'password': password,
        }
        response = self.test_client.post(
            url,
            headers=headers,
            data=json.dumps(data)
        )
        data = json.loads(response.data)
        return data.get('access_token')
