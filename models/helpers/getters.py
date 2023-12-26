from configuration.config import db
from models.tables.precincts import Precinct
from models.tables.relationships.ballots_races_join import BallotsRacesJoin
from models.tables.relationships.precincts_users_join import PrecinctsUsersJoin
from models.tables.relationships.precincts_zips_join import PrecinctsZipsJoin
from models.tables.relationships.races_candidates_join import RacesCandidatesJoin
from models.tables.relationships.voters_races_voted import VotersRacesVoted
from models.tables.users import User
from models.tables.elections import Election
from models.tables.races import Race
from models.tables.roles import Role
from models.tables.voters import Voter
from models.tables.candidates import Candidate
from models.tables.ballots import Ballot
from models.tables.zipcodes import ZipCode
from models.tables.relationships.users_roles_join import UsersRolesJoin
from models.tables.relationships.users_voters_join import UsersVotersJoin


def get_precincts():
    return Precinct.query.all()


def get_users():
    return User.query.all()


def get_elections():
    return Election.query.all()


def get_races():
    return Race.query.all()


def get_roles():
    return Role.query.all()


def get_voters():
    return Voter.query.all()


def get_candidates():
    return Candidate.query.all()


def get_ballots():
    return Ballot.query.all()

def get_zips():
    return ZipCode.query.all()

def get_poll_managers():
    return db.session.query(User.user_id, User.username, User.email, UsersRolesJoin.role_id).join(UsersRolesJoin,
                                                                                                  User.user_id == UsersRolesJoin.user_id).filter_by(
        role_id=2).all()


def get_precincts_with_managers():
    return db.session.query(Precinct, Precinct.precinct_id, Precinct.voting_location,
                            Precinct.state_election_office_contact_address, User.username).join(PrecinctsUsersJoin,
                                                                                                Precinct.precinct_id == PrecinctsUsersJoin.precinct_id,
                                                                                                isouter=True).join(User,
                                                                                                                   PrecinctsUsersJoin.user_id == User.user_id,
                                                                                                                   isouter=True).all()
def get_precinct_with_zips(precinct_id):
    return db.session.query(ZipCode, ZipCode.zip_id, ZipCode.zip, ZipCode.zip_plus_4_start, ZipCode.zip_plus_4_end).join(PrecinctsZipsJoin,
                                                                ZipCode.zip_id == PrecinctsZipsJoin.zip_id,
                                                                isouter=True).filter_by(precinct_id=precinct_id).all()

def get_users_with_voters():
    return db.sesion.query(User, User.user_id, User.username, User.email, Voter.voter_id, Voter.first_name,
                           Voter.last_name, Voter.middle_name, Voter.phone, Voter.address, Voter.address_2,
                           Voter.zip_code).join(UsersVotersJoin, User.user_id == UsersVotersJoin.user_id).join(Voter,
                                                                                                               UsersVotersJoin.voter_id == Voter.voter_id).all()



def get_election(election_id):
    return Election.query.filter_by(election_id=election_id).first()


def get_race_with_candidates():
    return db.session.query(Race, Race.race_id, Race.name, Candidate.candidate_id, Candidate.first_name,
                            Candidate.last_name, Candidate.party, Candidate.incumbent).join(RacesCandidatesJoin,
                                                                                            Race.race_id == RacesCandidatesJoin.race_id,
                                                                                            isouter=True).join(
        Candidate, RacesCandidatesJoin.candidate_id == Candidate.candidate_id, isouter=True).all()


def get_ballot_with_races(ballot_id):
    return db.session.query(Race, Race.race_id, Race.name).join(BallotsRacesJoin,
                                                                Race.race_id == BallotsRacesJoin.race_id,
                                                                isouter=True).filter_by(ballot_id=ballot_id).all()

def get_ballot_with_races_voter(ballot_id):
    return db.session.query(Race, Race.race_id, Race.name).join(BallotsRacesJoin,
                                                                Race.race_id == BallotsRacesJoin.race_id,
                                                                isouter=True).filter_by(ballot_id=ballot_id).all()


def get_race(race_id):
    return Race.query.filter_by(race_id=race_id).first()


def get_ballot_race_join(race_id):
    return BallotsRacesJoin.query.filter_by(race_id=race_id).first()


def get_race_candidate_join(candidate_id):
    return RacesCandidatesJoin.query.filter_by(candidate_id=candidate_id).first()

def get_unassigned_races(ballot_id):
    return db.session.query(Race, Race.race_id, Race.name).join(BallotsRacesJoin,
                                                                Race.race_id == BallotsRacesJoin.race_id,
                                                                isouter=True).filter(Ballot.ballot_id != ballot_id)


def get_assigned_candidates(race_id):
    return db.session.query(Candidate, Candidate.candidate_id, Candidate.first_name, Candidate.last_name,
                            Candidate.party, Candidate.incumbent, Candidate.description).join(RacesCandidatesJoin,
                                                                       Candidate.candidate_id == RacesCandidatesJoin.candidate_id).filter_by(
        race_id=race_id)


def get_unassigned_candidates():
    return db.session.query(Candidate, Candidate.candidate_id, Candidate.first_name, Candidate.last_name,
                            Candidate.party, Candidate.incumbent).join(RacesCandidatesJoin,
                                                                       Candidate.candidate_id == RacesCandidatesJoin.candidate_id,
                                                                       isouter=True).filter_by(race_id=None)
def get_user_role_id(user_id):
    role = UsersRolesJoin.query.filter_by(user_id=user_id).first()
    return role.role_id

def get_pending_voters():
    return (
        Voter.query
        .filter(Voter.pending == True)
        .all()
    )


def get_candidate(candidate_id):
    return Candidate.query.filter_by(candidate_id=candidate_id).first()




def get_precinct(precinct_id):
    return Precinct.query.filter_by(precinct_id=precinct_id).first()



def get_ballot(ballot_id):
    return Ballot.query.filter_by(ballot_id=ballot_id).first()

def get_ballots_with_election_and_precinct():
    return db.session.query(Ballot.ballot_id, Ballot.name, Election.start_datetime, Election.end_datetime, Precinct.voting_location, Election.title) \
            .join(Precinct, Ballot.precinct_id == Precinct.precinct_id) \
            .join(Election, Ballot.election_id == Election.election_id)

def get_ballots_with_elections(precinct_id):
    return db.session.query(Ballot.ballot_id, Ballot.name, Election.election_id, Election.title, Election.start_datetime, Election.end_datetime) \
            .join(Election, Ballot.election_id == Election.election_id).filter(Ballot.precinct_id == precinct_id)


def get_ballot_from_election(election_id):
    return Ballot.query.filter_by(election_id=election_id).first()

def get_ballots_with_election_and_precinct_for_poll_manager(uid):
    return db.session.query(Ballot.ballot_id, Ballot.name, Ballot.start_datetime, Ballot.end_datetime, Precinct.voting_location, Election.title, PrecinctsUsersJoin.precinct_id, PrecinctsUsersJoin.user_id) \
            .join(Precinct, Ballot.precinct_id == Precinct.precinct_id) \
            .join(Election, Ballot.election_id == Election.election_id) \
            .join(PrecinctsUsersJoin, Ballot.precinct_id == PrecinctsUsersJoin.precinct_id) \
            .filter_by(user_id=uid)


def get_unassigned_zips():
    return db.session.query(ZipCode, ZipCode.zip_id, ZipCode.zip, ZipCode.zip_plus_4_start,
                            ZipCode.zip_plus_4_end).join(PrecinctsZipsJoin,
                                                         ZipCode.zip_id == PrecinctsZipsJoin.zip_id,
                                                         isouter=True).filter_by(precinct_id=None).all()


def get_zip(zip_id):
    return ZipCode.query.filter_by(zip_id=zip_id).first()


def get_precinct_zip_join(zip_id):
    return PrecinctsZipsJoin.query.filter_by(zip_id=zip_id).first()


def get_voter_zip(voter_id):
    voter = Voter.query.filter_by(voter_id=voter_id).first()
    voter_zip = voter.zip_code[:5]
    plus4 = int(voter.zip_code[6:])
    zips = ZipCode.query.filter_by(zip=voter_zip).all()
    zipid = 0
    for zip in zips:
        if int(zip.zip_plus_4_start) <= plus4 and int(zip.zip_plus_4_end) >= plus4:
            zipid = zip.zip_id
            break
    return zipid


def get_races_from_ballot(ballot_id):
    return db.session.query(Ballot.ballot_id, Ballot.name, Race.race_id, Race.name) \
            .join(BallotsRacesJoin, Ballot.ballot_id == BallotsRacesJoin.ballot_id) \
            .join(Race, BallotsRacesJoin.race_id == Race.race_id).filter(Ballot.ballot_id == ballot_id)


def get_races_already_voted(voter_id):
    return db.session.query(VotersRacesVoted.race_id).filter(VotersRacesVoted.voter_id == voter_id).all()