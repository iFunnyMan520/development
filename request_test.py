import requests
from components.users.models import User
from components.advert.models import Car, Advt
from server import db, app

response = requests.post('https://weblabapi.com/ads/list',
                         data={'limit': 36, 'page': 1, 'sortBy': "dateDesc",
                         'status': "Published", 'type': "paid"})

commit_data = response.json()

model = ''
i = 0
count = 0

while count < 35:
    seo = commit_data['paidAds'][count]['seo']
    count += 1
    r = requests.post('https://weblabapi.com/ads/getBySeo', data={'seo': seo})
    c_data = r.json()

    if list(c_data['ad'].keys())[7] == 'brand':
        brand = c_data['ad']['brand']['name']
    if list(c_data['ad'].keys())[8] == 'product':
        model = c_data['ad']['product']['model']
    title = c_data['ad']['titleCompiled']
    description = c_data['ad']['description']
    phone = c_data['ad']['user']['phones'][0]['phone']
    user_name = c_data['ad']['user']['name']
    price = c_data['ad']['price']

    one = Advt(name=title, user=User(phone=phone, name=user_name), car=Car(
        brand=brand, model=model),
                 description=description,
                 price=price)

    if __name__ == "__main__":
        with app.app_context():
            db.session.add_all([one])
            db.session.commit()



