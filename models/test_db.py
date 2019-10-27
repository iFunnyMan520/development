from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    code = db.Column(db.String)


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    manifacture = db.Column(db.String(100))
    year = db.Column(db.DateTime)


class Advt(db.Model):
    __tablename__ = 'advt'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='users')
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    car = db.relationship('Car', backref='cars')
    description = db.Column(db.String(350))
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)


