class AbstractBadRequest(Exception):
    code = None
    msg = None
    detail = None

    def __init__(self):
        self._assertion()

    def _assertion(self):
        assert type(self.code) is int, "Exception's code should be int"
        assert type(self.msg) is str, "Exception's msg should be str"
        assert type(self.reason) is str, "Exception's reason should be str"

    def __str__(self):
        return f"Exception {self.__class__.__name__}"


class InvalidAcceptHeader(AbstractBadRequest):
    msg = "Invalid Accept header"
    code = 405

    def __init__(self, expected):
        self.expected = expected
        super(InvalidAcceptHeader, self).__init__()

    @property
    def reason(self):
        return f"Accept header should be '{self.expected}'"


class InvalidContentType(AbstractBadRequest):
    msg = "Invalid Content-Type"
    code = 405

    def __init__(self, expected):
        self.expected = expected
        super(InvalidContentType, self).__init__()

    @property
    def reason(self):
        return f"Content-Type should be '{self.expected}'"


class InvalidRequestBody(AbstractBadRequest):
    msg = "Invalid request"
    code = 400

    def __init__(self, field_name):
        self.field_name = field_name
        super(InvalidRequestBody, self).__init__()

    @property
    def reason(self):
        return f"The following field is invalid or missing: '{self.field_name}'"
