from flask import Response

from helpers.forms import Reg_Form, Login_form, Password_form
from helpers.error_helper import _Get_error


def Get_form(ty="login"):
    forms = {
        'login': Login_form,
        'register': Reg_Form,
        'password': Password_form
    }
    return forms.get(ty, Login_form)()


def Respond(content, status, err_type=None, ty="Err"):
    if ty == "Err":
        if err_type is None:
            err_type = 'REQUEST'
        return _Get_error(content, err_type, status)
    else:
        return Response('"Content": "{}"'.format(content), status=status, mimetype='application/json')
