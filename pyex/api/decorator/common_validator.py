from functools import wraps
import cgi
from accept_types import AcceptableType
from flask import request

from pyex.api.exception.exception import *

ALLOWED_ACCEPTS = ('application/json',)
ALLOWED_CONTENT_TYPES = ('application/json', 'multipart/form-data')


def header_check(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not any([AcceptableType(request.headers.get('Accept', '')).matches(accept) for accept in ALLOWED_ACCEPTS]):
            raise InvalidAcceptHeader(' or '.join(ALLOWED_ACCEPTS))
        mimetype, _ = cgi.parse_header(request.headers.get('Content-Type', ''))
        if request.method == "POST" and mimetype not in ALLOWED_CONTENT_TYPES:
            raise InvalidContentType(' or '.join(ALLOWED_CONTENT_TYPES))
        return f(*args, **kwargs)

    return decorated_function
