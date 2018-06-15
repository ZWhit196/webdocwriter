import json

from data.db_integ import Query_Interface as QI
from data.excel_integ import ExcelWriter
import models


def Get_user(identifier):
    if type(identifier) is str:
        filters = {'name': identifier.lower()}
    elif type(identifier) is int:
        filters = {'uid': identifier}
    else:
        raise ValueError("`uid` Number or String `name` is allowed only.")
    return QI(models.User, filters=filters, first=True).Fetch()


def Is_user(identifier):
    if Get_user(identifier) is not None:
        return True
    return False


def New_user(name, password):
    u = models.User(name, password)
    u.commit_self()
    u.create_directory()
    return u


# ========================

def ExcelCreator(data, user):
    data = json.loads(data)
    fname = list(data.keys())[0]
    json_data = data[fname]
    print(json_data)
    
    EW = ExcelWriter(fname, username=user.name)
    EW.Array_to_frame(json_data)
    
    success = "yes"
    return success