from flask import request, redirect, url_for, flash
from models.helpers.getters import get_candidate, get_race_candidate_join
from configuration.config import db
from models.tables.relationships.races_candidates_join import RacesCandidatesJoin


def process_candidate_assignment():
    race = request.args.get('race')
    candidate = request.args.get('candidate_id')
    user = request.args.get('user')
    action = request.args.get('action')
    candidate_info = get_candidate(candidate)
    assignment = get_race_candidate_join(candidate)
    if action == "remove":
        db.session.delete(assignment)
        db.session.commit()
        flash("Candidate " + candidate_info.first_name + " " + candidate_info.last_name + " has been removed from race.")
    elif action == "add":
        if assignment:
            assignment.race_id = race
        else:
            assignment = RacesCandidatesJoin(
                candidate_id=candidate,
                race_id=race
            )
        db.session.add(assignment)
        db.session.commit()
        flash("Candidate" + candidate_info.first_name + " " + candidate_info.last_name + " has been added to the race.")
    return redirect(url_for('app_assign_candidates', race=race, user=user))
