from flask import Blueprint, jsonify

from pyex.api.exception.exception import AbstractBadRequest

error_handler = Blueprint('ErrorHandler', __name__)


def register_exception_handler(app):
    @app.errorhandler(AbstractBadRequest)
    def basic_error(e):
        return jsonify({
            "msg": e.msg,
            "reason": e.reason,
            "code": e.code
        }), e.code

    @app.errorhandler(404)
    def not_found_error(e):
        return jsonify({
            "msg": "Resource not found",
            "reason": "Resource not found",
            "code": 404
        }), 404


    @app.errorhandler(500)
    def not_found_error(e):
        return jsonify({
            "msg": "There was an error, please try again",
            "reason": "Server error",
            "code": 500
        }), 500

    return app
