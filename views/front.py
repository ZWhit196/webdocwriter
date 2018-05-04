from flask import Blueprint, request, flash, redirect # jsonify, abort
from flask.templating import render_template
# from flask.helpers import url_for
# from flask_login import login_required, login_user, logout_user, current_user

# import forms
# from helpers import Respond

front_router = Blueprint('front', __name__, template_folder='templates')


@front_router.route("/", methods=['GET'])
def home():
    return render_template("front/index.html")
