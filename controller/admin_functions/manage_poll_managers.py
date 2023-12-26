from flask import render_template, request, flash, redirect, url_for
from models.tables.relationships.users_roles_join import UsersRolesJoin
from models.helpers.getters import get_poll_managers
from models.tables.users import User
from controller.navigation import admin_routes
from models.forms.polling_manager_form import PollingManagerForm
from configuration.config import db
import bcrypt
from datetime import datetime

def manage_poll_managers(user):
    routes = admin_routes(user)
    poll_managers = get_poll_managers()
    form = PollingManagerForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            email_address = request.form['email_address']
            username = request.form['username']
            salt = bcrypt.gensalt()
            bcrypt_bytes = (request.form['password']).encode('utf-8')
            bcrypt_hash = bcrypt.hashpw(bcrypt_bytes, salt)
            session = db.session()
            now = datetime.now()
            new_user = User(
                username=username,
                password_digest=bcrypt_hash,
                email=email_address,
                created_at=now.strftime("%Y/%m/%d %H:%M:%S"),
                last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
                authenticated=0)
            session.add(new_user)
            session.flush()
            new_role_join = UsersRolesJoin(user_id=new_user.user_id, role_id=2)
            session.add(new_role_join)
            session.commit()
            flash("Poll manager created successfully.")
            return redirect(url_for("app_manage_poll_managers", user=user))
        else:
            flash("Unable to add poll manager. Please try again.")

    return render_template("admin_pages/managepollmanagers.html", poll_managers=poll_managers, user=user, routes=routes, form=form)
