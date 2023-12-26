from flask import redirect, url_for, flash
from flask_login import logout_user
from configuration.config import db
from models.tables.users import User


def logout(user):
    usr = User.query.filter_by(user_id=user).first()
    usr.authenticated = False
    db.session.commit()
    logout_user()
    flash("Logout successful.")
    return redirect(url_for('app_home'))
