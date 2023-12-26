from flask import render_template
from controller.navigation import admin_routes
from models.helpers.getters import get_assigned_candidates, get_unassigned_candidates, get_race


def assign_candidates(user, race):
    routes = admin_routes(user)
    assigned_candidates = get_assigned_candidates(race)
    current_race = get_race(race)
    unassigned_candidates = get_unassigned_candidates()
    return render_template('admin_pages/assigncandidates.html', current_race=current_race, routes=routes, user=user, assigned_candidates=assigned_candidates, unassigned_candidates=unassigned_candidates)
