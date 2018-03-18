#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app
from app.models import db
from app.views import api_bp
import config

app.config.from_object(config)
app.register_blueprint(api_bp, url_prefix='/api')
db.init_app(app)

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
    }
