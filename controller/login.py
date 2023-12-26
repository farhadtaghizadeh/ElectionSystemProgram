from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user
from controller.navigation import guest_routes
from configuration.config import db
from models.forms.login_form import LoginForm
from models.tables.users import User
import bcrypt




def login():
    routes = guest_routes()
    form = LoginForm()
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        usr = User.query.filter_by(username=username).first()
        if usr and bcrypt.checkpw(password.encode("utf-8"), usr.password_digest.encode("utf-8")):
            usr.authenticated = True
            db.session.commit()
            login_user(usr)
            return redirect(url_for('app_view_profile', user=usr.user_id))
        else:
            error = 'You have entered an incorrect username or password, please try again.'
    if error is not None:
        flash(error)
    return render_template('login.html', form=form, error=error, routes=routes)
