import requests
from components.users.models import User
from components.advert.models import Car, Advt

response = requests.post('https://weblabapi.com/ads/list',
                         data={'limit': 36, 'page': 1, 'sortBy': "dateDesc",
                         'status': "Published", 'type': "paid"})

commit_data = response.json()


count = 0

while count < 35:
    seo = commit_data['paidAds'][count]['seo']

    r = requests.post('https://weblabapi.com/ads/getBySeo', data={'seo': seo})
    c_data = r.json()
    brand = c_data['ad']['brand']
    #if list(c_data['ad'].keys())[28] == 'product':
    model = c_data['ad']['product']['model']
    #else:
        #continue
    title = c_data['ad']['title']
    description = c_data['ad']['description']
    phone = c_data['ad']['user']['phones'][0]['phone']
    user_id = c_data['ad']['user']['id']
    count += 1
    print(model)


