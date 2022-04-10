import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # TODO Load credentials from environment variables
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/garuda_pms'
    SQLALCHEMY_TRACK_MODIFICATIONS = False