# Add func
from data.db_integ import Query_Interface as QI
import models


def Get_user(identifier):
    if type(identifier) is str:
        filters = {'name': identifier}
    elif type(identifier) is int:
        filters = {'uid': identifier}
    else:
        raise ValueError("`uid` Number or String `name` is allowed only.")
    return QI(models.User, filters=filters, first=True).Fetch()


def Is_user(identifier):
    if Get_user(identifier) is not None:
        return True
    return False
