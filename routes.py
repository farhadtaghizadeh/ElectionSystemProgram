from flask import Flask, send_from_directory, request
from flask_login import login_required, LoginManager, fresh_login_required

from controller.admin_functions.assign_races import assign_races
from controller.admin_functions.assign_zips import assign_zips
from controller.admin_functions.manage_races import manage_races
from controller.admin_functions.admin_panel import admin_panel
from controller.admin_functions.manage_elections import manage_elections
from controller.admin_functions.manage_poll_managers import manage_poll_managers
from controller.admin_functions.manage_precincts import manage_precincts
from controller.admin_functions.manage_candidates import manage_candidates
from controller.admin_functions.process_race_assignment import process_race_assignment
from controller.admin_functions.process_candidate_assignment import process_candidate_assignment
from controller.admin_functions.assign_candidates import assign_candidates
from controller.admin_functions.manage_zips import manage_zips
from controller.admin_functions.process_zip_assignment import process_zip_assignment
from controller.home import home
from controller.login import login
from controller.manager_functions.manager_panel import manager_panel
from controller.register import register
from controller.voter_functions.view_candidates import view_candidates
from controller.voter_functions.view_profile import viewprofile
from controller.change_password import changepassword
from controller.manager_functions.approve import approve
from controller.manager_functions.process_approval import process_approval
from controller.manager_functions.search import search
from controller.manager_functions.ballots_manager import ballots_manager
from controller.logout import logout
from controller.relogin import relogin
from controller.change_address import changeaddress
from controller.test import test
from controller.voter_functions.vote_for_candidate import vote_for_candidate
from controller.voter_functions.vote_races import vote_races
from models.tables.users import User
from controller.admin_functions.assign_poll_manager import assign_manager
from controller.admin_functions.process_manager_assignment import process_manager_assignment
from controller.admin_functions.manage_ballots import manage_ballots
from controller.admin_functions.ballot_update_election import ballot_update_election
from controller.admin_functions.process_ballot_update_election import process_ballot_update_election
from controller.admin_functions.ballot_update_precinct import ballot_update_precinct
from controller.admin_functions.process_ballot_update_precinct import process_ballot_update_precinct


app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = "app_login"
login_manager.login_message = u"Please log in to access this page."
login_manager.refresh_view = "app_re_login"
login_manager.needs_refresh_message = "To protect your account, please revalidate your info."


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


login_manager.init_app(app)


@app.route('/')
def app_home():
    return home()


@app.route('/static/<path:path>')
def send_report(path):
    return send_from_directory('static', path)


@app.route('/login/', methods=['GET', 'POST'])
def app_login():
    return login()


@app.route('/relogin/', methods=['GET', 'POST'])
def app_re_login():
    return relogin()


@app.route('/logout/', methods=['GET'])
@login_required
def app_logout():
    user = request.args.get('user')
    return logout(user)


@app.route('/register/', methods=['GET', 'POST'])
def app_register():
    return register()


@app.route('/user_panel/', methods=['GET'])
@login_required
def app_view_profile():
    user = request.args.get('user')
    return viewprofile(user)


@app.route('/user_panel/change_password/', methods=['GET', 'POST'])
@fresh_login_required
def app_change_password():
    user = request.args.get('username')
    return changepassword(user)


@app.route('/user_panel/change_address/', methods=['GET', 'POST'])
@fresh_login_required
def app_change_address():
    user = request.args.get('username')
    return changeaddress(user)

@app.route('/manager_panel/', methods=['GET', 'POST'])
@login_required
def app_manager_panel():
    user = request.args.get('user')
    return manager_panel(user)


@app.route('/manager_panel/voter_requests/', methods=['GET', 'POST'])
@login_required
def app_manager_approve():
    user = request.args.get('user')
    return approve(user)

@app.route('/manager_panel/search_voters/', methods=['GET', 'POST'])
@login_required
def app_manager_search():
    user = request.args.get('user')
    return search(user)

@app.route('/manager_panel/ballots/', methods=['GET', 'POST'])
@login_required
def app_ballots_manager():
    user = request.args.get('user')
    return ballots_manager(user)


@app.route('/admin_panel/voter_requests/', methods=['GET', 'POST'])
@login_required
def app_admin_approve():
    user = request.args.get('user')
    return approve(user)


@app.route('/process-approval/', methods=['GET', 'POST'])
@login_required
def app_process_approval():
    return process_approval()


@app.route('/admin_panel/', methods=['GET', 'POST'])
@fresh_login_required
def app_admin_panel():
    user = request.args.get('user')
    return admin_panel(user)

@app.route('/admin_panel/search_voters/', methods=['GET', 'POST'])
@login_required
def app_admin_search():
    user = request.args.get('user')
    return search(user)


@app.route('/admin_panel/manage_elections/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_elections():
    user = request.args.get('user')
    return manage_elections(user)


@app.route('/admin_panel/manage_ballots/assign_races/', methods=['GET', 'POST'])
@fresh_login_required
def app_assign_races():
    user = request.args.get('user')
    ballot = request.args.get('ballot')
    return assign_races(user, ballot)

@app.route('/admin_panel/manage_races/assign_candidates/', methods=['GET', 'POST'])
@fresh_login_required
def app_assign_candidates():
    user = request.args.get('user')
    race = request.args.get('race')
    return assign_candidates(user, race)




@app.route('/admin_panel/manage_precincts/assign_zips/', methods=['GET', 'POST'])
@fresh_login_required
def app_assign_zips():
    user = request.args.get('user')
    precinct = request.args.get('precinct')
    return assign_zips(user, precinct)


@app.route('/admin_panel/manage_precincts/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_precincts():
    user = request.args.get('user')
    return manage_precincts(user)

@app.route('/admin_panel/manage_zips/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_zips():
    user = request.args.get('user')
    return manage_zips(user)


@app.route('/admin_panel/manage_poll_managers/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_poll_managers():
    user = request.args.get('user')
    return manage_poll_managers(user)


@app.route('/admin_panel/manage_races/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_races():
    user = request.args.get('user')
    return manage_races(user)


@app.route('/admin_panel/manage_candidates/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_candidates():
    user = request.args.get('user')
    return manage_candidates(user)


@app.route('/admin_panel/manage_precincts/assign_manager/', methods=['GET', 'POST'])
@fresh_login_required
def app_assign_manager():
    return assign_manager()


@app.route('/admin_panel/manage_ballots/', methods=['GET', 'POST'])
@fresh_login_required
def app_manage_ballots():
    user = request.args.get('user')
    return manage_ballots(user)

@app.route('/admin_panel/manage_ballots/update_election/', methods=['GET', 'POST'])
@fresh_login_required
def app_ballot_update_election():
    user = request.args.get('user')
    ballotid = request.args.get('ballotid')
    ballotname = request.args.get('ballotname')
    return ballot_update_election(user, ballotid, ballotname)

@app.route('/admin_panel/manage_ballots/update_precinct/', methods=['GET', 'POST'])
@fresh_login_required
def app_ballot_update_precinct():
    user = request.args.get('user')
    ballotid = request.args.get('ballotid')
    ballotname = request.args.get('ballotname')
    return ballot_update_precinct(user, ballotid, ballotname)

@app.route('/process_ballot_update_election/', methods=['GET', 'POST'])
@fresh_login_required
def app_process_ballot_update_election():
    return process_ballot_update_election()

@app.route('/process_ballot_update_precinct/', methods=['GET', 'POST'])
@fresh_login_required
def app_process_ballot_update_precinct():
    return process_ballot_update_precinct()

@app.route('/process_manager_assignment/', methods=['GET', 'POST'])
@login_required
def app_process_manager_assignment():
    return process_manager_assignment()


@app.route('/process_zip_assignment/', methods=['GET', 'POST'])
@login_required
def app_process_zip_assignment():
    return process_zip_assignment()


@app.route('/process_race_assignment/', methods=['GET','POST'])
@login_required
def app_process_race_assignment():
    return process_race_assignment()


@app.route('/process_candidate_assignment/', methods=['GET','POST'])
@login_required
def app_process_candidate_assignment():
    return process_candidate_assignment()


@app.route('/test/', methods=['GET', 'POST'])
def app_test():
    return test()


@app.route('/vote_for_candidate/', methods=['GET', 'POST'])
@login_required
def app_vote_for_candidate():
    candidate_id = request.args.get('candidate_id')
    voter_id = request.args.get('voter')
    race_id = request.args.get('race')
    user_id = request.args.get('user')
    ballot_id = request.args.get('ballot')
    return vote_for_candidate(candidate_id, voter_id, race_id, user_id, ballot_id)

@app.route('/user_panel/vote_races/', methods=['GET', 'POST'])
@login_required
def app_user_panel_vote_races():
    user_id = request.args.get('user')
    ballot_id = request.args.get('ballot')
    voter_id = request.args.get('voter')
    return vote_races(ballot_id, voter_id, user_id)

@app.route('/user_panel/vote_races/view_candidates/', methods=['GET', 'POST'])
@login_required
def app_view_candidates():
    ballot_id = request.args.get('ballot')
    user_id = request.args.get('user')
    race_id = request.args.get('race')
    voter_id = request.args.get('voter')
    return view_candidates(race_id, voter_id, user_id, ballot_id)
