from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_precincts

def ballot_update_precinct(user, ballotid, ballotname):
    routes = admin_routes(user)
    precincts = get_precincts()

    return render_template('admin_pages/ballotupdateprecinct.html', precincts=precincts, routes=routes, user=user, ballotid=ballotid, ballotname=ballotname)
