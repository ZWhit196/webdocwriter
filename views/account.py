from flask import Blueprint, request, flash, redirect # jsonify, abort
from flask.templating import render_template
from flask.helpers import url_for
from flask_login import login_required, login_user, logout_user, current_user

from data import Is_user
from helpers import Respond, Get_form

account_router = Blueprint('account', __name__, template_folder='templates')


@account_router.route("/login", methods=['GET','POST'])
def login():
    form = Get_form('login')
    if form.validate_on_submit():

        ### Login code ###

        flash("You are logged in.")
        return redirect(url_for('front.home'))

    if form.password.errors:
        for err in form.password.errors:
            flash(err)
    return render_template("account/login.html", form=form)


@account_router.route("/register", methods=['GET','POST'])
def register():
    form = Get_form('register')
    if form.validate_on_submit():

        ### Register code ###

        flash("User has been registered and logged in.")
        return redirect(url_for('front.home'))

    if form.email.errors or form.password.errors:
        for err in form.email.errors:
            flash(err)
        for err in form.password.errors:
            flash(err)
    return render_template("account/login.html", form=form)


@account_router.route("/account", methods=['GET','POST'])
@login_required
def account():
    form = Get_form('password')
    if form.validate_on_submit():

        ### Account code ###

        flash("Password has been updated.")
        return redirect(url_for('account.account'))

    if form.password.errors:
        for err in form.password.errors:
            flash(err)
    return render_template("account/login.html", form=form)
