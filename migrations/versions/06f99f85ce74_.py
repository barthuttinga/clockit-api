"""empty message

Revision ID: 06f99f85ce74
Revises: 1cc051a1ee1a
Create Date: 2018-03-12 11:02:52.379938

"""
from alembic import op
import sqlalchemy as sa
from faker import Faker
from models import Customer, Project, Task
from app import create_app
from flask_sqlalchemy import SQLAlchemy


# revision identifiers, used by Alembic.
revision = '06f99f85ce74'
down_revision = '1cc051a1ee1a'
branch_labels = None
depends_on = None

def upgrade():
    fake = Faker('nl_NL')
    fake.seed(1)
    app = create_app('config')
    db = SQLAlchemy()

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


def downgrade():
    pass
