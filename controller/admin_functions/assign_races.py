from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_ballot_with_races, get_unassigned_races, get_ballot


def assign_races(user, ballot):
    routes = admin_routes(user)
    assigned_races = get_ballot_with_races(ballot)
    current_ballot = get_ballot(ballot)
    unassigned_races = get_unassigned_races(ballot)
    return render_template('admin_pages/assignraces.html', current_ballot=current_ballot, routes=routes, user=user, assigned_races=assigned_races, unassigned_races=unassigned_races)
