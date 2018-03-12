# ClockIt API
REST API for ClockIt time registration app.

## Installation
- Run `git clone git@github.com:barthuttinga/clockit-api.git` to clone the project
- Run `cd clockit-api` to cd into the project directory
- Run `pip install -r requirements.txt` to install dependencies
- Run `python migrate.py db upgrade` to create the SQLite-database schema populated with fake data
- Run `python run.py` to start the app on [http://127.0.0.1:5000/api/](http://127.0.0.1:5000/api/)

## Resource endpoints
Method | URI | Description
--- | --- | ---
GET | http://127.0.0.1:5000/api/customers/ | List of customers
GET | http://127.0.0.1:5000/api/customers/x | Customer with ID x
GET | http://127.0.0.1:5000/api/projects/ | List of projects
GET | http://127.0.0.1:5000/api/projects/x | Project with ID x
GET | http://127.0.0.1:5000/api/customers/x/projects | List of projects for customer with ID x
GET | http://127.0.0.1:5000/api/tasks/ | List of tasks
GET | http://127.0.0.1:5000/api/tasks/x | Task with ID x
GET | http://127.0.0.1:5000/api/projects/x/tasks/ | List of tasks for project with ID x
