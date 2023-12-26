from flask import redirect, url_for, flash
from configuration.config import db
from models.helpers.getters import get_ballot
from models.tables.relationships.voters_races_voted import VotersRacesVoted
from models.tables.votes import Vote


def vote_for_candidate(candidate_id, voter_id, race_id, user_id, ballot_id):
    ballot = ballot_id.strip("\"")
    voter = voter_id.strip("\"")
    race = race_id.strip("\"")
    user = user_id.strip("\"")
    candidate = candidate_id.strip("\"")
    bal = get_ballot(ballot_id)
    election_id = bal.election_id
    vote = Vote(
        ballot_id=int(ballot),
        candidate_id=int(candidate),
        race_id=int(race),
        election_id=election_id
    )
    db.session.add(vote)
    db.session.flush()
    voted = VotersRacesVoted(
        ballot_id=int(ballot),
        race_id=int(race),
        voter_id=int(voter)
    )
    db.session.add(voted)
    db.session.commit()
    flash("Your vote has been submitted.")
    return redirect(url_for('app_user_panel_vote_races', ballot=ballot, user=user, voter=voter_id))
