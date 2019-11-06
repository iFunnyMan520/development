from flask_sqlalchemy import SQLAlchemy


class DevConfig:
    DEBUG = True
    ENV = 'development'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///foo.db'
    SECRET_KEY = 'mysecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


db = SQLAlchemy()
conf = DevConfig()
