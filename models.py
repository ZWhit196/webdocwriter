import datetime
import os

from data.database import db
from passlib.hash import pbkdf2_sha512


class User(db.Model):
    uid = db.Column('uid', db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    account_created = db.Column(db.DateTime())
    is_admin = db.Column(db.Boolean(), nullable=False, default=False)
    last_login = db.Column(db.DateTime())
    # _games = db.relationship('Game', secondary=User_games, backref=db.backref('User_games', lazy='dynamic'),
    #                          lazy='dynamic', primaryjoin='User_games.c.uid==User.uid',
    #                          secondaryjoin='User_games.c.gid==Game.gid', cascade="save-update, merge, delete")

    def __init__(self, name, password):
        self.name = name.lower()
        self.set_password(password)
        self.account_created = datetime.datetime.now()
        self.account_active = True
        self.is_admin = False
        self.last_login = datetime.datetime.now()

    def __repr__(self):
        return '<User: {}>'.format(self.name)

    # functions for login manager
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.uid)
    # End login manager func.

    def set_admin(self):
        """ sets a user to admin status """
        self.is_admin = True
        self.commit_self()

    def set_password(self, password):
        """ hashes and salts a new password """
        self.password = pbkdf2_sha512.hash(password, rounds=200000, salt_size=16)

    def verify_password(self, password):
        """ verifies a password """
        return pbkdf2_sha512.verify(password, self.password)

    def update_password(self, password):
        """ sets and saves a password """
        self.set_password(password)
        self.commit_self()

    def update_login(self):
        """ updates time since last login """
        self.last_login = datetime.datetime.now()
        self.commit_self()

    def delete_user(self):
        """ delete the user """
        db.session.delete(self)
        db.session.commit()

    def commit_self(self):
        """ commit changes to the database """
        db.session.add(self)
        db.session.commit()

    def create_directory(self):
        """ creates a directory for users docs """
        directory = "./docs/{}".format()
        if not os.path.exists(directory):
            os.makedirs(directory)


class Documents(db.Model):
    did = db.Column('did', db.Integer, primary_key=True, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey(User.uid))
    doc_name = db.Column(db.String(256), nullable=False)
    doc_type = db.Column(db.String(8), nullable=False)
    doc_created = db.Column(db.DateTime())
    doc_path = db.Column(db.Text, nullable=False)

    def __init__(self, name, typ, created, path):
        self.doc_name = name
        self.doc_type = typ
        self.doc_created = created
        self.doc_path = path
