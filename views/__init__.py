from views.account import account_router
from views.create import create_router
from views.front import front_router


def Get_routes():
    routes = [
        front_router,
        account_router,
        create_router
    ]
    return routes
