from flask import request, render_template, flash
from models.forms.search_form import SearchForm
from controller.navigation import admin_routes, manager_routes, guest_routes
from models.tables.voters import Voter
from models.tables.relationships.users_roles_join import UsersRolesJoin
def search(user):
    filter = UsersRolesJoin.query.filter_by(user_id=user).first()
    if filter.role_id == 1:
        routes = admin_routes(user)
    elif filter.role_id == 2:
        routes = manager_routes(user)
    else:
        routes=guest_routes()
    form = SearchForm()
    if request.method == 'POST':
        if ('first_name' in request.form):
            first_name = request.form['first_name']
            search = "%{}%".format(first_name)
            voters = Voter.query.filter(Voter.first_name.like(search)).all()
        elif ('last_name' in request.form):
            last_name = request.form['last_name']
            search = "%{}%".format(last_name)
            voters = Voter.query.filter(Voter.last_name.like(search)).all()
        elif ('middle_name' in request.form):
            middle_name = request.form['middle_name']
            search = "%{}%".format(middle_name)
            voters = Voter.query.filter(Voter.middle_name.like(search)).all()
        elif ('zip_code' in request.form):
            zip_code = request.form['zip_code']
            search = "%{}%".format(zip_code)
            voters = Voter.query.filter(Voter.zip_code.like(search)).all()
        elif ('polling_station' in request.form):
            zip_code = request.form['zip_code']
            search = "%{}%".format(zip_code)
            voters = Voter.query.filter(Voter.zip_code.like(search)).all()
        else:
            flash("Invalid search terms")
            return render_template('search.html', form=form, routes=routes, user=user)
        return render_template('admin_pages/votersearchresults.html', voters=voters, form=form, routes=routes, user=user)

    return render_template('search.html', form=form, routes=routes, user=user)