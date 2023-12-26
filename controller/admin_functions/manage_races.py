from flask import render_template, request, flash, redirect, url_for
from models.forms.race_form import RaceForm
from models.tables.races import Race
from models.helpers.getters import get_races
from controller.navigation import admin_routes
from configuration.config import db
def manage_races(user):
    routes = admin_routes(user)
    races = get_races()
    form = RaceForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form['name']
            race = Race(
                name=name,
            )
            db.session.add(race)
            db.session.commit()
            flash("Race added successfully.")
            return redirect(url_for("app_manage_races", user=user))
        else:
            flash("Unable to add race. Please try again.")

    return render_template("admin_pages/manageraces.html", races=races, user=user, routes=routes, form=form)


