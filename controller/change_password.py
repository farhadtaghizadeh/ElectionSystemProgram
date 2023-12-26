from flask import request, flash, url_for, render_template, redirect
from models.forms.change_password_form import ChangePasswordForm
from configuration.config import db
from controller.navigation import guest_routes, voter_routes, admin_routes
from models.tables.relationships.users_roles_join import UsersRolesJoin
from models.tables.users import User
from datetime import datetime
import bcrypt
routes1 = guest_routes()

def changepassword(user):
    usr = User.query.filter_by(username=user).first()
    role = UsersRolesJoin.query.filter_by(user_id=usr.user_id).first()
    if role.role_id == 3:
        routes = voter_routes(str(usr.user_id))
    elif role.role_id == 1:
        routes = admin_routes(str(usr.user_id))
    else:
        routes = routes1
    form = ChangePasswordForm()
    error = None
    if request.method == "POST" and form.validate_on_submit():
        current_password = request.form['current_password']
        new_password = request.form['password']

        if bcrypt.checkpw(current_password.encode("utf-8"), usr.password_digest.encode("utf-8")):
            salt = bcrypt.gensalt()
            password_bytes = new_password.encode('utf-8')
            password_hash = bcrypt.hashpw(password_bytes, salt)
            now = datetime.now()
            usr.password_digest = password_hash
            usr.last_modified = now.strftime("%Y/%m/%d %H:%M:%S")
            db.session.commit()
            flash("Your password has been successfully updated.")
            return redirect(url_for('app_view_profile', user=usr.user_id))
        else:
            error = 'You have entered an incorrect password, please try again.'
    if error is not None:
        flash(error)
    return render_template('changepassword.html', form=form, error=error, routes=routes)
