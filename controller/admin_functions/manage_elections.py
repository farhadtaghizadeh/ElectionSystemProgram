from flask import render_template, request, redirect, url_for, flash
from models.tables.elections import Election
from controller.navigation import admin_routes
from models.forms.election_form import ElectionForm
from models.helpers.getters import get_elections
from configuration.config import db


def manage_elections(user):
    routes = admin_routes(user)
    elections = get_elections()
    form = ElectionForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            start_time = request.form['start_time']
            start_date = request.form['start_date']
            end_time = request.form['end_time']
            end_date = request.form['end_date']
            title = request.form['title']
            election = Election(
                title=title,
                start_datetime=(start_date + " " + start_time),
                end_datetime=(end_date + " " + end_time)
            )
            db.session.add(election)
            db.session.commit()
            flash("Election added successfully.")
            return redirect(url_for("app_manage_elections", user=user))
        else:
            flash("Unable to add election. Please try again.")
    return render_template("admin_pages/manageelections.html", elections=elections, user=user, routes=routes, form=form)
