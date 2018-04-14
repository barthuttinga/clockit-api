import os

from config_dev import ConfigDev

basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigTest(ConfigDev):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    SERVER_NAME = '127.0.0.1:5000'
