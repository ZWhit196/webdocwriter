import os
import traceback

from flask import Flask, request
from flask_login import LoginManager
from flask.templating import render_template
from flask_wtf.csrf import CSRFProtect, CSRFError

from data.database import db
from helpers import Respond
from models import User
import views


def GenerateKey():
    return os.urandom(64)


def Settings():
    settings = {
        'DEBUG': True,
        'JS_TEST': False,
        'SECRET_KEY': 'a',#GenerateKey(),
        'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///DataStore.db',
        'WTF_CSRF_SECRET_KEY': GenerateKey()
    }
    return settings


def setup_database(app):
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)

    conf = Settings()
    for key in conf:
        app.config[key] = conf[key]

    db.init_app(app)

    # login manager
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'account.login'

    @login_manager.user_loader   # keeps the user in the session
    def load_user(uid):
        return User.query.get(int(uid))

    CSRFProtect().init_app(app)  # CSRF PROTECTION

    @app.errorhandler(400)
    @app.errorhandler(403)
    @app.errorhandler(404)
    @app.errorhandler(500)
    @app.errorhandler(CSRFError)
    def error_loading(ex):
        cd = 400
        msg = "There was an issue in your request, try refreshing your page and trying again."
        if ex.code:
            cd = ex.code
        if cd == 500:
            traceback.print_exc()
        if request.method == 'POST' or "static" in request.url:
            return Respond(msg, ex.code, ty="Err")
        return render_template('error.html', err=cd, msg=msg)

    routes = views.Get_routes()
    for route in routes:
        app.register_blueprint(route)

    return app


def run_app():
    app = create_app()
    if not os.path.isfile('DataStore.db'):
        setup_database(app)
    app.run(host="0.0.0.0", port=8000)
    return app
