from flask import render_template
from models.tables.users import User
from controller.navigation import manager_routes


def manager_panel(user):
    routes = manager_routes(user)
    usr = User.query.filter_by(user_id=user).first()
    return render_template('manager_pages/managerportal.html', user=usr, routes=routes)
