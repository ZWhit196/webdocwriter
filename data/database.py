from flask_sqlalchemy import SQLAlchemy

from models import User

db = SQLAlchemy()


def Get_user(name, all=False):
    if all:
        return User.query.all()
    return User.query.filter("")



class Query_Interface():

    Main_table = None
    Join = []
    Filters = {}
    First = True

    def __init__(self, tbl, joins=[], filters={}, first=True):
        self.Main_table = tbl
        self.First = first
        if type(joins) is list:
            self.Join = joins
        elif type(joins) is str:
            self.Join = [joins]
        else:
            raise TypeError("`joins` parameter accepts list of str or str")
        if type(filters) is not dict:
            raise TypeError("`filters` parameter accepts python dict `{<filter>: <value>}` or `{<filter>: [<value1>,...]`")
