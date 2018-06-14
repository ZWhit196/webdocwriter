from flask import Blueprint, request, flash, jsonify  # , redirect, abort
from flask.templating import render_template
# from flask.helpers import url_for
from flask_login import login_required, current_user

from helpers import Respond
from data import ExcelCreator

create_router = Blueprint('create', __name__, template_folder='templates')


@create_router.route("/create/document", methods=['GET', 'POST'])
@login_required
def document():
    if request.method == "GET":
        return render_template("create/document.html")
    flash("Posted")
    return Respond("Posted", 200)


@create_router.route("/create/spreadsheet", methods=['GET', 'POST'])
@login_required
def spreadsheet():
    if request.method == "GET":
        return render_template("create/spreadsheet.html")
    
    end = ExcelCreator(request.data.decode("utf-8"), current_user)
    
    return jsonify("Passed")
