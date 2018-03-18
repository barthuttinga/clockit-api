# ClockIt API
REST API for ClockIt time registration app.

## Installation
- Run `git clone git@github.com:barthuttinga/clockit-api.git` to clone the
project and cd into the project directory
- Run `pipenv install --dev` to create a virtual environment and install dependencies
- Run `pipenv shell` to enter a shell within the virtual environment
- Run `export FLASK_APP=clockit_api.py` and `export FLASK_DEBUG=1` to point
Flask to the app and enabled debugging mode
- Run `flask db upgrade` create the SQLite-database and/or upgrade the schema
- Run `python load_fixtures.py` if you want to populate the database with some
data fixtures
- Run `flask run` to start the app on
[http://127.0.0.1:5000/api/](http://127.0.0.1:5000/api/)

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
