from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_assigned_elections, get_unassigned_elections, get_ballot


def assign_elections(user, ballot):
    routes = admin_routes(user)
    assigned_elections = get_assigned_elections(ballot)
    current_ballot = get_ballot(ballot)
    unassigned_elections = get_unassigned_elections(ballot)
    return render_template('admin_pages/assigncandidates.html', current_race=current_race, routes=routes, user=user, assigned_candidates=assigned_candidates, unassigned_candidates=unassigned_candidates)
