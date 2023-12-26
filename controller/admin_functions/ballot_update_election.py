from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_elections

def ballot_update_election(user, ballotid, ballotname):
    routes = admin_routes(user)
    elections = get_elections()

    return render_template('admin_pages/ballotupdateelection.html', elections=elections, routes=routes, user=user, ballotid=ballotid, ballotname=ballotname)
