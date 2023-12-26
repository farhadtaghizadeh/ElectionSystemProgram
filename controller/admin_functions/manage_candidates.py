from flask import render_template, request, flash, redirect, url_for
from models.forms.candidate_form import CandidateForm
from models.tables.candidates import Candidate
from controller.navigation import admin_routes
from configuration.config import db
from models.helpers.getters import get_candidates
def manage_candidates(user):
    routes = admin_routes(user)
    form = CandidateForm()
    candidates = get_candidates()
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            party = request.form['party']
            description = request.form['description']
            incumbent = 'incumbent' in request.form
            candidate = Candidate(
                first_name=first_name,
                last_name=last_name,
                party=party,
                incumbent=incumbent,
                description=description
            )
            db.session.add(candidate)
            db.session.commit()
            flash("Candidate added successfully.")
            return redirect(url_for("app_manage_candidates", user=user))
        else:
            flash("Unable to add candidate. Please try again.")

    return render_template("admin_pages/managecandidates.html", candidates=candidates, user=user, routes=routes, form=form)


