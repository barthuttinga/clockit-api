#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import create_app, db
from config import Config

app = create_app(Config)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
    }
