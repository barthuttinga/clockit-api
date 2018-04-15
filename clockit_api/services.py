from .models import Customer, Project, Task, db


class AddUpdateDelete():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self, resource):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class CustomerService(AddUpdateDelete):
    def findAll(self):
        return db.session.query(Customer).all()

    def find(self, id):
        return Customer.query.get_or_404(id)


class ProjectService(AddUpdateDelete):
    def findAll(self):
        return Project.query.all()

    def find(self, id):
        return Project.query.get_or_404(id)


class TaskService(AddUpdateDelete):
    def findAll(self):
        return Task.query.all()

    def find(self, id):
        return Task.query.get_or_404(id)


customer_service = CustomerService()
project_service = ProjectService()
task_service = TaskService()
