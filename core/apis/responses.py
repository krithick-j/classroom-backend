from flask import Response, jsonify, make_response
from http import HTTPStatus


class APIResponse(Response):
    @classmethod
    def respond(cls, data, status_code=HTTPStatus.OK):
        return make_response(jsonify(data=data), status_code)
