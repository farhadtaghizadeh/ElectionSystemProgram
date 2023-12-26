from flask import request, flash, url_for, render_template, redirect
from models.forms.change_address_form import ChangeAddressForm
from configuration.config import db
from controller.navigation import voter_routes
from models.tables.relationships.users_voters_join import UsersVotersJoin
from models.tables.users import User
from datetime import datetime
from models.tables.voters import Voter




def changeaddress(user):
    usr = User.query.filter_by(username=user).first()
    routes1 = voter_routes(str(usr.user_id))
    voterjoin = UsersVotersJoin.query.filter_by(user_id=usr.user_id).first()
    voter = Voter.query.filter_by(voter_id=voterjoin.voter_id).first()
    form = ChangeAddressForm()
    error = None
    if request.method == "POST" and form.validate_on_submit():
        now = datetime.now()
        voter.address = request.form["address"]
        voter.address2 = request.form["address2"]
        voter.city = request.form["city"]
        voter.state = request.form["state"]
        if voter.zip_code != request.form["zip_code"]:
            voter.zip_code = request.form["zip_code"]
            voter.zip_last_modified = now.strftime("%Y/%m/%d %H:%M:%S")
        voter.last_modified = now.strftime("%Y/%m/%d %H:%M:%S")
        db.session.commit()
        flash("Your address has been successfully updated.")
        return redirect(url_for('app_view_profile', user=usr.user_id))
    elif request.method == "POST" and not form.validate_on_submit():
        error = 'You have entered invalid information, please try again.'
    return render_template('changeaddress.html', form=form, error=error, voter=voter, routes=routes1)
