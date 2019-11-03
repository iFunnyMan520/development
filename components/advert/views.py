import json

from components.advert.models import Advt


def advt():
    adverts = Advt.query.all()
    adverts_list = list()
    for adverts_iterator in adverts:
        adverts_dict = {
            'id': adverts_iterator.id,
            'name': adverts_iterator.name,
            'user': {
                'user_id': adverts_iterator.user.id,
                'user_name': adverts_iterator.user.phone
            },
            'car': {
                'car_id': adverts_iterator.car.id,
                'car_brand': adverts_iterator.car.brand,
                'car_model': adverts_iterator.car.model,
                'car_manufacture': adverts_iterator.car.manufacture,
                'car_year': adverts_iterator.car.year
            },
            'description': adverts_iterator.description,
            'price': adverts_iterator.price,
            'created_at': adverts_iterator.created_at,
        }
        adverts_list.append(adverts_dict)

    return json.dumps(adverts_list)