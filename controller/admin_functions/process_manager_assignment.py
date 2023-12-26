from flask import request, redirect, url_for, flash
from models.tables.relationships.precincts_users_join import PrecinctsUsersJoin
from models.tables.precincts import Precinct
from configuration.config import db
def process_manager_assignment():
    precinct = request.args.get('precinct')
    polling_manager = request.args.get('poll_manager')
    user = request.args.get('user')
    prec = Precinct.query.filter_by(precinct_id=precinct).first()
    assignment = PrecinctsUsersJoin.query.filter_by(precinct_id=prec.precinct_id).first()
    if assignment:
        assignment.user_id = polling_manager

    else:
        assignment = PrecinctsUsersJoin(
            user_id=polling_manager,
            precinct_id=prec.precinct_id
        )
    db.session.add(assignment)
    db.session.commit()
    flash("Precinct" + precinct + " has been updated.")
    return redirect(url_for('app_manage_precincts',user=user))