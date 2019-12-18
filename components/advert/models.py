from settings import db


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(100))
    manufacture = db.Column(db.String(100))
    year = db.Column(db.Integer)

    def __repr__(self):
        return '<Car %r>' % self.brand


class Advt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='advt')
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'))
    car = db.relationship('Car', backref='advt')
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    created_at = db.Column(db.Integer)
