from settings import db


class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    manufacture = db.Column(db.String(100))
    year = db.Column(db.Integer)


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
    created_at = db.Column(db.Integer)
