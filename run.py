#!/usr/bin/env python
# -*- coding: utf-8 -*-

from clockit_api.app import create_app


app = create_app('config')


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
