from components.users.models import *
from components.advert.models import *

from server import db, app


if __name__ == "__main__":
    with app.app_context():
        first = Car(brand='Ford', model='Mustang', manufacture='USA',
                    year=1969)
        second = Car(brand='Ford', model='Mustang', manufacture='USA',
                     year=2014)
        third = Car(brand='Lexus', model='RX350', manufacture='Japan',
                    year=2014)
        db.session.add_all([first, second, third])
        db.session.commit()

        one = Advt(name='Sale', user_id=1, car_id=1, description='Cheep, '
                                                                 'powerful '
                                                                 'car',
                   price=23.351, created_at=2019)
        two = Advt(name='Sale', user_id=1, car_id=2, description='Cheep, '
                                                                 'powerful '
                                                                 'car',
                   price=40.895, created_at=2019)
        three = Advt(name='Sale', user_id=2, car_id=3, description='Cheep, '
                                                                 'powerful '
                                                                 'car',
                   price=51.843, created_at=2019)
        db.session.add_all([one, two, three])
        db.session.commit()
