from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_precinct_with_zips, get_unassigned_zips, get_precinct


def assign_zips(user, precinct):
    routes = admin_routes(user)
    assigned_zips = get_precinct_with_zips(precinct)
    current_precinct = get_precinct(precinct)
    unassigned_zips = get_unassigned_zips()
    return render_template('admin_pages/assignzips.html', current_precinct=current_precinct, routes=routes, user=user, assigned_zips=assigned_zips, unassigned_zips=unassigned_zips)
