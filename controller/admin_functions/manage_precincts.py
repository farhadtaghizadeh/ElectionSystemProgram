from flask import render_template, request, flash, redirect, url_for
from models.tables.precincts import Precinct
from models.helpers.getters import get_precincts_with_managers
from controller.navigation import admin_routes
from models.forms.precinct_form import PrecinctForm
from models.forms.assign_poll_manager_form import AssignPollManager
from configuration.config import db


def manage_precincts(user):
    routes = admin_routes(user)
    precincts = get_precincts_with_managers()
    form = PrecinctForm()
    form2 = AssignPollManager()
    if request.method == 'POST':
        if form.validate_on_submit():
            voting_location = request.form['voting_location']
            election_office = request.form['election_office']
            precinct = Precinct(
                voting_location=voting_location,
                state_election_office_contact_address=election_office
            )
            db.session.add(precinct)
            db.session.commit()
            flash("Precinct added successfully.")
            return redirect(url_for("app_manage_precincts", user=user))
        else:
            flash("Unable to add precinct. Please try again.")

    return render_template("admin_pages/manageprecincts.html", precincts=precincts, user=user, routes=routes, form=form,
                           form2=form2)
