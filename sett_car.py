from components.users.models import *
from components.advert.models import *

from server import db, app


if __name__ == "__main__":
    with app.app_context():
        ads_owner = User(phone='invalid_phone_number')
        db.session.add(ads_owner)
        db.session.commit()

        first = Car(brand='Ford', model='Mustang', manufacture='USA',
                    year=1969)
        second = Car(brand='Ford', model='Mustang', manufacture='USA',
                     year=2014)
        third = Car(brand='Lexus', model='RX350', manufacture='Japan',
                    year=2014)
        db.session.add_all([first, second, third])
        db.session.commit()

        one = Advt(name='Sale', car_id=first.id, user_id=ads_owner.id,
                   description='Cheep, powerful car',
                   price=23.351, created_at=2019)
        two = Advt(name='Sale', user_id=ads_owner.id, car_id=second.id,
                   description='Cheep, powerful car',
                   price=40.895, created_at=2019)
        three = Advt(name='Sale', user_id=ads_owner.id, car_id=third.id,
                     description='Cheep, powerful car',
                     price=51.843, created_at=2019)
        db.session.add_all([one, two, three])
        db.session.commit()
