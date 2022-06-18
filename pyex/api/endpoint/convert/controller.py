from zipfile import BadZipFile

from flask import current_app
from flask import jsonify, Blueprint, request

from pyex.api.decorator.common_validator import header_check
from pyex.api.exception.exception import InvalidRequestBody
from pyex.reader import Reader
from pyex.writer import RawWriter

excel_api = Blueprint('excel', __name__)


@excel_api.route('/upload', methods=['POST'])
@header_check
def excel():
    file = request.files.get('excel', None)
    if file is None:
        raise InvalidRequestBody('excel')
    try:
        reader = Reader(file)
        writer = RawWriter()
        return jsonify({
            "data": writer.write(
                reader.read(exclude=current_app.config['exclude'],
                            default=current_app.config['default'],
                            ffill=current_app.config['ffill']))
        })
    except BadZipFile:
        raise InvalidRequestBody('excel')
