from flask import render_template, request, flash, redirect, url_for
from models.tables.zipcodes import ZipCode
from models.helpers.getters import get_zips
from controller.navigation import admin_routes
from models.forms.zip_form import ZipForm
from configuration.config import db


def manage_zips(user):
    routes = admin_routes(user)
    zips = get_zips()
    form = ZipForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            zip = request.form['zip']
            zip4start = request.form['zip4start']
            zip4end = request.form['zip4end']
            new_zip = ZipCode(
                zip=zip,
                zip_plus_4_start=zip4start,
                zip_plus_4_end=zip4end
            )
            db.session.add(new_zip)
            db.session.commit()
            flash("Zip added successfully.")
            return redirect(url_for("app_manage_zips", user=user))
        else:
            flash("Unable to add zip. Please try again.")

    return render_template("admin_pages/managezips.html", zips=zips, user=user, routes=routes, form=form)
