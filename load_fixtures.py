from faker import Faker
from app.models import Customer, Project, Task
from app import app, db


def load_fixtures():
    fake = Faker('nl_NL')
    fake.seed(1)

    for i in range(0, 4):
        customer = Customer(fake.company())
        db.session.add(customer)
        for j in range(0, 3):
            project = Project(fake.word(), customer)
            db.session.add(project)
            for j in range(0, 2):
                task = Task(fake.sentence(), project)
                db.session.add(task)
    db.session.commit()


if __name__ == '__main__':
    load_fixtures()