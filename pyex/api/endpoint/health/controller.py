from flask import Blueprint,jsonify

from pyex import VERSION
from pyex.api.decorator.common_validator import header_check

health_api = Blueprint('health', __name__)


@health_api.route('', methods=['GET'])
@header_check
def health():
    return jsonify({
        "status": "HEALTHY",
        "version": VERSION
    })
