import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Required for CSRF
    SECRET_KEY = 'test'
    # Database credentials
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/garuda_pms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False