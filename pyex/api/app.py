from flask import Flask

from pyex.api.endpoint.route import api
from pyex.api.exception.handler import register_exception_handler

DEFAULT_CONFIG = {
    "exclude": None,
    "ffill": "",
    "default": "undefined"
}


def create_app(configurations={}):
    app = Flask(__name__)
    configs = DEFAULT_CONFIG
    configs.update(configurations)
    for key, val in configs.items():
        app.config[key] = val
    app.register_blueprint(api, url_prefix="/api")
    register_exception_handler(app)
    return app
