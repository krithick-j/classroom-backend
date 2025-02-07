from flask import Response, jsonify, make_response
from http import HTTPStatus


class APIResponse(Response):
    @classmethod
    def respond(cls, data, status_code=HTTPStatus.OK):
        return make_response(jsonify(data=data), status_code)

    @classmethod
    def respond_error(cls, message, error, status_code=HTTPStatus.BAD_REQUEST):
        return make_response(jsonify(message=message, error=error), status_code)