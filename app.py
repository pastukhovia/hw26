from flask import Flask
from main.views import main_blueprint
from errorhandler.errorhandler import error_handler
from apis.api import api_blueprint

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.register_blueprint(main_blueprint)
    app.register_blueprint(error_handler)
    app.register_blueprint(api_blueprint)

    return app
