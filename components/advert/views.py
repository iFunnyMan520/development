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
                'id': adverts_iterator.user.id,
                'name': adverts_iterator.user.phone
            },
            'car': {
                'id': adverts_iterator.car.id,
                'brand': adverts_iterator.car.brand,
                'model': adverts_iterator.car.model,
                'manufacture': adverts_iterator.car.manufacture,
                'year': adverts_iterator.car.year,
                'image': 'https://vectorskey.com/wp-content/uploads'
                         '/2019/01/police-car.png'
            },
            'description': adverts_iterator.description,
            'price': adverts_iterator.price,
            'created_at': adverts_iterator.created_at,
        }
        adverts_list.append(adverts_dict)

    return json.dumps(adverts_list)
