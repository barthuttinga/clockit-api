from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from .models import db
from .security import jwt


def create_app(configuration):
    app = Flask('clockit_api')
    app.config.from_object(configuration)

    db.init_app(app)

    Migrate(app, db)

    # from .schemas import ma
    ma = Marshmallow()
    ma.init_app(app)

    from .views import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    jwt.init_app(app)

    return app
