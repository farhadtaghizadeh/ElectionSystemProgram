from flask import render_template, request
from models.helpers.getters import get_poll_managers, get_precincts

def assign_manager():
    user = request.args.get('user')
    precinct = request.args.get('precinct')
    poll_managers_list = get_poll_managers()


    return render_template('admin_pages/assignpollmanagers.html', list=poll_managers_list, user=user, precinct=precinct)