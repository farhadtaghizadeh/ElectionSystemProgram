from flask import render_template
from controller.navigation import voter_approved_routes
from models.helpers.getters import get_assigned_candidates, get_race


def view_candidates(race_id, voter_id, user_id, ballot_id):
    routes=voter_approved_routes(user_id)
    assigned_candidates = get_assigned_candidates(race_id)
    current_race = get_race(race_id)
    return render_template('viewcandidates.html', ballot=ballot_id, current_race=current_race, routes=routes, user=user_id, assigned_candidates=assigned_candidates, voter=voter_id)