from flask import render_template
from controller.navigation import admin_routes, manager_routes, guest_routes
from models.helpers.getters import get_pending_voters
from models.tables.relationships.users_roles_join import UsersRolesJoin


def approve(user):
    filter = UsersRolesJoin.query.filter_by(user_id=user).first()
    if filter.role_id == 1:
        routes = admin_routes(user)
    elif filter.role_id == 2:
        routes = manager_routes(user)
    else:
        routes = guest_routes()
    voters = get_pending_voters()
    return render_template('admin_pages/approve.html', user=user, voters=voters, routes=routes)



