from settings import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String)
    code = db.Column(db.String)
    name = db.Column(db.String)

    def __repr__(self):
        return '<User %r>' % self.name
