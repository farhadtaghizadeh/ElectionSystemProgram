from flask import render_template
from models.tables.users import User
from controller.navigation import admin_routes


def admin_panel(user):
    routes = admin_routes(user)
    usr = User.query.filter_by(user_id=user).first()
    return render_template('admin_pages/adminportal.html', user=usr, routes=routes)
