from flask import render_template, request, url_for, redirect, flash
from models.forms.ballot_form import BallotForm
from controller.navigation import admin_routes
from models.helpers.getters import get_ballots
from models.tables.ballots import Ballot
from models.helpers.getters import get_elections
from models.helpers.getters import get_precincts
from models.helpers.getters import get_ballots_with_election_and_precinct
from configuration.config import db

def manage_ballots(user):
    form = BallotForm(elections=get_elections())
    form.elections.choices = [(e.election_id, e.title) for e in get_elections()]
    form.precincts.choices = [(p.precinct_id, p.voting_location) for p in get_precincts()]
    routes = admin_routes(user)
    ballots = get_ballots_with_election_and_precinct()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            election_id = request.form['elections']
            precinct_id = request.form['precincts']
            ballot = Ballot(
                name=name,
                election_id=election_id,
                precinct_id=precinct_id,
                activated=False,
            )
            db.session.add(ballot)
            db.session.commit()
            flash("Ballot added successfully.")
            return redirect(url_for("app_manage_ballots", user=user))
        else:
            flash("Unable to add ballot. Please try again.")

    return render_template("admin_pages/manageballots.html", user=user, form=form, routes=routes, ballots=ballots)