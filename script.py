from components.users.models import *
from components.advert.models import *

from server import db, app


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
