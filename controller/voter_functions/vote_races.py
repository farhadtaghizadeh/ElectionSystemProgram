from flask import render_template, request, flash
from models.helpers.getters import get_ballot_with_races_voter, get_races_already_voted
from controller.navigation import voter_approved_routes
from configuration.config import db
from models.forms.vote_form import VoteForm


def vote_races(ballot_id, voter_id, user_id):
    routes = voter_approved_routes(user_id)
    assigned_races = get_ballot_with_races_voter(ballot_id)
    assigned_votes = []
    voted_races = get_races_already_voted(voter_id)
    for voted in voted_races:
        assigned_votes.append(voted[0])
    return render_template("votepage.html", voted_races=assigned_votes, races=assigned_races, ballot=ballot_id, user=user_id, voter=voter_id, routes=routes)
