from flask import request, redirect, url_for, flash
from models.tables.ballots import Ballot
from configuration.config import db

def process_ballot_update_precinct():
    user = request.args.get('user')
    ballot = request.args.get('ballot')
    precinct = request.args.get('precinct')
    bal = Ballot.query.filter_by(ballot_id=ballot).first()
    bal.precinct_id = precinct
    db.session.add(bal)
    db.session.commit()
    flash(f'Ballot {bal.name} has been updated.')
    return redirect(url_for('app_manage_ballots',user=user))