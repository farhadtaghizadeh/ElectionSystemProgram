from flask import render_template, url_for, redirect
from models.helpers.getters import get_voter_zip, get_precinct_zip_join, get_precinct, get_ballots_with_elections
from models.tables.ballots import Ballot
from models.tables.elections import Election
from models.tables.relationships.users_roles_join import UsersRolesJoin
from models.tables.relationships.users_voters_join import UsersVotersJoin
from models.tables.voters import Voter
from models.tables.users import User
from controller.navigation import voter_routes, voter_approved_routes


def viewprofile(user):
    role = UsersRolesJoin.query.filter_by(user_id=user).first()
    if role.role_id == 1:
        return redirect(url_for('app_admin_panel', user=user))

    if role.role_id == 2:
        return redirect(url_for('app_manager_panel', user=user))

    if role.role_id == 3:
        vj = UsersVotersJoin.query.filter_by(user_id=user).first()
        voter = Voter.query.filter_by(voter_id=vj.voter_id).first()
        if voter.approved:
            routes = voter_approved_routes(user)
        else:
            routes = voter_routes(user)
        zip = get_voter_zip(voter.voter_id)
        precinct_id = get_precinct_zip_join(zip).precinct_id
        precinct = get_precinct(precinct_id)
        voter_user = User.query.filter_by(user_id=user).first()
        elections = get_ballots_with_elections(precinct_id)
        return render_template('voterportal.html', elections=elections, precinct=precinct, voter=voter, user=voter_user, routes=routes)