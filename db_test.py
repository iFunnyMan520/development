from server import db, app
from components.users.models import User
from components.advert.models import Car, Advt


def create_user(user_name):
    user = User(name=user_name)
    db.session.add(user)
    db.session.commit()
    return user


def create_car(brand):
    car = Car(brand=brand)
    db.session.add(car)
    db.session.commit()
    return car


def create_add(user, car, price):
    ads = Advt(user=user, car=car, price=price)
    db.session.add(ads)
    db.session.commit()
    return ads


def delete_ads(ads):
    db.session.delete(ads)
    db.session.commit()


def test():
    with app.app_context():
        user_name = 'user1'
        brand_name = 'Audi'
        price = 12000

        user = create_user(user_name)
        car = create_car(brand_name)
        ad_test = create_add(user, car, price)

        assert ad_test is not None

        count_of_user = User.query.all()
        count_of_car = Car.query.all()
        count_of_ad = Advt.query.all()

        assert len(count_of_user) == 1
        assert len(count_of_car) == 1
        assert len(count_of_ad) == 1

        delete_ads(user)
        delete_ads(car)
        delete_ads(ad_test)

        count_of_user = User.query.all()
        count_of_car = Car.query.all()
        count_of_ad = Advt.query.all()

        assert not len(count_of_user)
        assert not len(count_of_car)
        assert not len(count_of_ad)
