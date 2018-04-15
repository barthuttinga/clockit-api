from . import AppTestCase
from ..models import Customer, Project, Team, User, db


class ModelsTestCase(AppTestCase):
    def test_create_team(self):
        data = {'name': 'My team'}
        team = Team(**data)
        assert team.id is None
        assert team.name == data.get('name')
        assert team.created_at is None
        assert len(team.users.all()) == 0

        db.session.add(team)
        db.session.commit()
        assert team.id is not None
        assert team.created_at is not None

    def test_create_user(self):
        team = Team(name='My team')
        data = {'username': 'Myself', 'team': team}
        user = User(**data)
        assert user.id is None
        assert user.username == data.get('username')
        assert user.created_at is None

        db.session.add(user)
        db.session.commit()
        assert user.id is not None
        assert user.created_at is not None

    def test_create_customer(self):
        team = Team(name='My team')
        data = {'name': 'My customer', 'team': team}
        customer = Customer(**data)
        assert customer.id is None
        assert customer.name == data.get('name')
        assert customer.created_at is None
        assert customer.team == team
        assert customer.team.id is None
        assert len(customer.projects.all()) == 0

        db.session.add(customer)
        db.session.commit()
        assert customer.id is not None
        assert customer.created_at is not None
        assert customer.team.id is not None

    def test_create_project_with_new_customer(self):
        customer = Customer(name='My customer', team=self.team)
        data = {'name': 'My project', 'customer': customer}
        project = Project(**data)
        assert project.name == data.get('name')
        assert project.created_at is None
        assert project.customer == customer
        assert len(customer.projects.all()) == 1

        db.session.add(project)
        db.session.commit()
        assert project.id is not None
        assert project.created_at is not None
        assert customer.id is not None
        assert customer.created_at is not None

    def test_create_project_with_existing_customer(self):
        customer = Customer(name='My customer', team=self.team)
        db.session.add(customer)
        db.session.commit()

        data = {'name': 'My project', 'customer': customer}
        project = Project(**data)
        assert project.name == data.get('name')
        assert project.created_at is None
        assert project.customer == customer
        assert len(customer.projects.all()) == 1

        db.session.add(project)
        db.session.commit()
        assert project.id is not None
        assert project.created_at is not None

    # def test_create_task_with_new_project_and_new_customer(self):
    #     customer = Customer(name='My customer')
    #     project = Project(name='My project', customer=customer)
    #     start = datetime.now()
    #     data = {'name': 'My task', 'start': start, 'project': project}
    #     task = Task(**data)
    #     assert task.name == data.get('name')
    #     assert task.created_at is None
    #     assert task.start == start
    #     assert task.project == project
    #     assert task.project.customer == customer
    #
    #     db.session.add(task)
    #     db.session.commit()
    #     assert task.id is not None
    #     assert task.created_at is not None
    #     assert project.id is not None
    #     assert project.created_at is not None
    #     assert customer.id is not None
    #     assert customer.created_at is not None
