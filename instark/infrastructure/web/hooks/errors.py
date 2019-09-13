from flask import Flask, jsonify
from traceback import format_tb
from werkzeug.exceptions import HTTPException


def register_error_handler(app: Flask):

    def handle_error(error):
        code = 500

        if isinstance(error, HTTPException):
            code = error.code or code

        exception = type(error).__name__
        traceback = format_tb(error.__traceback__)

        return jsonify(error={
            'exception': exception,
            'message': str(error),
            'trace': traceback
        }), code

    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, handle_error)
