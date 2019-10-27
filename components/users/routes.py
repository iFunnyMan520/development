from flask import Flask

from components.users import views


def install(app: Flask):
    app.add_url_rule(
        '/phone/', view_func=views.confirm, methods=['GET'])
    app.add_url_rule(
        '/phone/confirm', view_func=views.confirm, methods=['POST'])
    app.add_url_rule(
        '/phone/confirm/enter', view_func=views.confirm, methods=['POST'])
