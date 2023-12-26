from flask import render_template, url_for, flash, redirect, request
from models.helpers.getters import get_ballots_with_election_and_precinct_for_poll_manager
from models.forms.activate_ballot_form import ActivateBallotForm
from models.tables.ballots import Ballot
from configuration.config import db
from datetime import datetime

def ballots_manager(user):
    ballots = get_ballots_with_election_and_precinct_for_poll_manager(user)
    form = ActivateBallotForm()
    current_datetime = datetime.now()
    if request.method == 'POST':
        if form.is_submitted():
            id = request.form['ballot_id']
            start_date = request.form['start_date']
            start_time = request.form['start_time']
            end_date = request.form['end_date']
            end_time = request.form['end_time']
            # print(f'id {id} start {start_date} {start_time} end {end_date} {end_time}')
            bal = Ballot.query.filter_by(ballot_id = id).first()
            bal.start_datetime = f'{start_date} {start_time}'
            bal.end_datetime = f'{end_date} {end_time}'
            db.session.add(bal)
            db.session.commit()
            flash("Updated Ballot Successfully.")
            return redirect(url_for("app_ballots_manager", user=user))
        else:
            flash("Unable to add ballot. Please try again.")

    return render_template('manager_pages/ballotsmanager.html', user=user, ballots=ballots, activate_form=form, current_datetime=current_datetime)