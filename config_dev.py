import os

from config import Config

basedir = os.path.abspath(os.path.dirname(__file__))


class ConfigDev(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}/clockit_dev.db'.format(basedir)
