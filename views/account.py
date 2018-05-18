from flask import Blueprint, request, flash, redirect # jsonify, abort
from flask.templating import render_template
from flask.helpers import url_for
from flask_login import login_required, login_user, logout_user, current_user

from data import Get_user, New_user
from helpers import Get_form  # Respond,

account_router = Blueprint('account', __name__, template_folder='templates')


@account_router.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("front.home"))


@account_router.route("/login", methods=['GET', 'POST'])
def login():
    form = Get_form('login')
    if form.validate_on_submit():
        u = Get_user(form.name.data)
        login_user(u)
        flash("You are logged in.")
        return redirect(url_for('front.home'))
    if form.password.errors:
        for err in form.password.errors:
            flash(err)
    if form.name.errors:
        for err in form.name.errors:
            flash(err)
    return render_template("account/login.html", form=form)


@account_router.route("/register", methods=['GET', 'POST'])
def register():
    form = Get_form('register')
    if form.validate_on_submit():
        u = New_user(form.name.data, form.password.data)
        login_user(u)
        flash("User has been registered and logged in.")
        return redirect(url_for('front.home'))
    if form.name.errors or form.password.errors:
        for err in form.name.errors:
            flash(err)
        for err in form.password.errors:
            flash(err)
    return render_template("account/register.html", form=form)


@account_router.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = Get_form('password')
    if form.validate_on_submit():
        # Account code
        flash("Password has been updated.")
        return redirect(url_for('account.account'))  # May need a details update page.
    if form.password.errors:
        for err in form.password.errors:
            flash(err)
    return render_template("account/account.html", form=form)

# TODO: Add a account detail change page thingy: Low priority
