from flask import Response

from helpers.error_helper import _Get_error


def Respond(content, status, err_type=None, ty="Err"):
    if ty == "Err":
        if err_type is None:
            err_type = 'REQUEST'
        return _Get_error(content, err_type, status)
    else:
        return Response('"Content": "{}"}'.format(content), status=status, mimetype='application/json')
