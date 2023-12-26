from flask import request, redirect, url_for, flash
from models.helpers.getters import get_zip, get_precinct_zip_join
from configuration.config import db
from models.tables.relationships.precincts_zips_join import PrecinctsZipsJoin


def process_zip_assignment():
    precinct = request.args.get('precinct')
    zip = request.args.get('zip_id')
    user = request.args.get('user')
    action = request.args.get('action')
    zip_info = get_zip(precinct)
    assignment = get_precinct_zip_join(zip)
    if action == "remove":
        db.session.delete(assignment)
        db.session.commit()
        flash("Zip " + zip_info.zip + " with range: " + zip_info.zip_plus_4_start + " - " + zip_info.zip_plus_4_end + " has been removed for the precinct.")
    elif action == "add":
        if assignment:
            assignment.precinct_id = precinct
        else:
            assignment = PrecinctsZipsJoin(
                zip_id=zip,
                precinct_id=precinct
            )
        db.session.add(assignment)
        db.session.commit()
        flash("Zip " + zip_info.zip + " with range: " + zip_info.zip_plus_4_start + " - " + zip_info.zip_plus_4_end + " has been added as a location for the precinct.")
    return redirect(url_for('app_assign_zips', precinct=precinct, user=user))
