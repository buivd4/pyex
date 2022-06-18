from flask import Blueprint

from pyex.api.endpoint.convert.controller import excel_api
from pyex.api.endpoint.health.controller import health_api

api = Blueprint('convert', __name__)

api.register_blueprint(excel_api, url_prefix="/convert")
api.register_blueprint(health_api, url_prefix="/health")
