from components.advert import views


def install(app):
    app.add_url_rule(
        '/advt/', view_func=views.advt, methods=['GET'])
