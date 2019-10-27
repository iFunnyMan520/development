import random
from flask import render_template, Flask

from components.users.routes import install as user_routes
from settings import conf, db

Random = int(random.random()*10000)


app = Flask(__name__)
app.config.from_object(conf)

db.init_app(app)


@app.route('/')
def main_page():
    return render_template('main.html')


if __name__ == "__main__":
    user_routes(app)
    app.run(debug=True)
