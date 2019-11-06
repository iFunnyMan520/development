import random
from flask import render_template, Flask

from components.users.routes import install as user_routes
from components.advert.routes import install as ads_routes
from settings import conf, db
from components.users.models import User
from components.advert.models import Advt, Car
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

Random = int(random.random()*10000)


app = Flask(__name__)
app.config.from_object(conf)

db.init_app(app)
admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Advt, db.session))
admin.add_view(ModelView(Car, db.session))


@app.route('/')
def main_page():
    return render_template('main.html')


if __name__ == "__main__":
    user_routes(app)
    ads_routes(app)
    app.run(debug=True)
