from flask import request, render_template, redirect, url_for, flash
from models.tables.voters import Voter
from datetime import datetime
from configuration.config import db
from models.helpers.getters import get_user_role_id

def process_approval():
    voter_id = request.args.get('voter_id')
    action = request.args.get('action')
    user = request.args.get('user')
    session = db.session()
    voter = session.query(Voter).filter(Voter.voter_id == voter_id).first()

    if voter:
        voter.pending = False
        voter.approved_date = datetime.now()
        if action == 'approve':
            flash("Voter" + voter.first_name + " " + voter.last_name + " has been approved.")
            voter.approved = True
            print("approved")
        elif action == 'deny':
            flash("Voter" + voter.first_name + " " + voter.last_name + " has been denied.")
            voter.approved = False
            print("denied")
        print(voter)
        session.commit()

    session.close()

    role_id = get_user_role_id(user)
    if role_id == 1:
        return redirect(url_for('app_admin_approve',user=user))
    else:
        return redirect(url_for('app_manager_approve', user=user))