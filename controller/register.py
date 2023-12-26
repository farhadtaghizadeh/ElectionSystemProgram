from models.forms.register_form import RegisterForm
from flask import request, flash, render_template
from controller.navigation import guest_routes
import bcrypt
from datetime import datetime
from models.tables.users import User
from models.tables.voters import Voter
from models.tables.relationships.users_voters_join import UsersVotersJoin
from models.tables.relationships.users_roles_join import UsersRolesJoin
from configuration.config import db


def register():
    routes = guest_routes()
    form = RegisterForm()
    if request.method == "POST" and form.validate_on_submit():
        usr = User.query.filter_by(username=request.form['username']).first()
        if usr is None:
            name = request.form['first_name']
            flash(
                'Thank you, {}. Your information has been submitted. It can take up to 5 days for your registration to be approved. Please wait to be notified by email.'.format(
                    name))
            salt = bcrypt.gensalt()
            bcrypt_bytes = (request.form['password']).encode('utf-8')
            bcrypt_hash = bcrypt.hashpw(bcrypt_bytes, salt)
            session = db.session()
            now = datetime.now()
            new_user = User(
                username=request.form['username'],
                password_digest=bcrypt_hash,
                email=request.form['email_address'],
                created_at=now.strftime("%Y/%m/%d %H:%M:%S"),
                last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
                authenticated=0)
            session.add(new_user)
            session.flush()
            new_voter = Voter(
                first_name=request.form['first_name'],
                middle_name=request.form['middle_name'],
                last_name=request.form['last_name'],
                date_of_birth=request.form['date_of_birth'],
                phone=request.form['phone_number'],
                address=request.form['address'],
                address_2=request.form['address2'],
                zip_code=request.form['zip_code'],
                last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
                zip_last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
                pending=True,
                approved=False,
                approved_date=None,
                document1_info=request.form['gov_id_1'],
                document1_type=request.form['gov_id_1_type'],
                document2_info=request.form['gov_id_2'],
                document2_type=request.form['gov_id_2_type'],
            )
            session.add(new_voter)
            session.flush()
            new_voter_join = UsersVotersJoin(voter_id=new_voter.voter_id, user_id=new_user.user_id)
            db.session.add(new_voter_join)
            session.flush()
            new_role_join = UsersRolesJoin(user_id=new_user.user_id, role_id=3)
            db.session.add(new_role_join)
            db.session.commit()

            return render_template('home.html', routes=routes)
        else:
            flash("Error: That username has already been registered.")
    else:
        print(form.form_errors)
    return render_template('register.html', form=form, routes=routes)
