from flask import request, redirect, url_for, flash
from models.helpers.getters import get_race, get_ballot_race_join
from models.tables.relationships.ballots_races_join import BallotsRacesJoin
from configuration.config import db


def process_race_assignment():
    ballot = request.args.get('ballot')
    race = request.args.get('race_id')
    user = request.args.get('user')
    action = request.args.get('action')
    race_info = get_race(race)
    assignment = get_ballot_race_join(race)
    if action == "remove":
        db.session.delete(assignment)
        db.session.commit()
        flash("Race" + race_info.name + " has been removed from ballot.")
    elif action == "add":
        if assignment:
            assignment.ballot_id = ballot
        else:
            assignment = BallotsRacesJoin(
                race_id=race,
                ballot_id=ballot
            )
        db.session.add(assignment)
        db.session.commit()
        flash("Race" + race_info.name + " has been updated.")
    return redirect(url_for('app_assign_races', ballot=ballot, user=user))
