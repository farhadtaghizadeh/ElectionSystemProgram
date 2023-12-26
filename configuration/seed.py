from models.tables.elections import Election
from models.tables.precincts import Precinct
from models.tables.races import Race
from models.tables.relationships.ballots_races_join import BallotsRacesJoin
from models.tables.relationships.precincts_users_join import PrecinctsUsersJoin
from models.tables.relationships.precincts_zips_join import PrecinctsZipsJoin
from models.tables.relationships.races_candidates_join import RacesCandidatesJoin
from models.tables.users import User
from models.tables.candidates import Candidate
from models.tables.relationships.users_roles_join import UsersRolesJoin
from models.tables.relationships.users_voters_join import UsersVotersJoin
from models.tables.voters import Voter
from models.tables.roles import Role
from models.tables.ballots import Ballot

from datetime import datetime

from models.tables.zipcodes import ZipCode

now = datetime.now()


def seed_db(db=None):
    role1 = Role(role_id=1,
                 role_name="admin",
                 role_permissions_level=10)
    db.session.add(role1)
    role2 = Role(role_id=2,
                 role_name="poll_manager",
                 role_permissions_level=5)
    db.session.add(role2)
    role3 = Role(role_id=3,
                 role_name="voter",
                 role_permissions_level=1)
    db.session.add(role3)
    db.session.flush()
    u1 = User(user_id=1,
              username='admin',
              password_digest=b'$2b$12$fhmZVqpMnKWLOmuMhUOkseDUNl/ZX236ny/WzckfyDjNe6xjAly3.',
              email='admin@admin.com',
              created_at=datetime.now(),
              last_modified=datetime.now())
    db.session.add(u1)

    u2 = User(user_id=2,
              username='jsmith',
              password_digest=b'$2b$12$fhmZVqpMnKWLOmuMhUOkseDUNl/ZX236ny/WzckfyDjNe6xjAly3.',
              email='jsmith@gmail.com',
              created_at=datetime.now(),
              last_modified=datetime.now(),
              )
    db.session.add(u2)
    u3 = User(user_id=3,
              username='bpoll',
              password_digest=b'$2b$12$QuQJUcnGbZVP968CT1vPquXOnX8WxkB0u62WJo3XUgSp82Yr02RQW',  # Bobby123!
              email='bobbypoller@bpolls.com',
              created_at=datetime.now(),
              last_modified=datetime.now(),
              )
    db.session.add(u3)
    u4 = User(
        user_id=4,
        username='jimmys',
        password_digest=b'$2b$12$QuQJUcnGbZVP968CT1vPquXOnX8WxkB0u62WJo3XUgSp82Yr02RQW',  # Bobby123!
        email='jimmy@jimmy.com',
        created_at=datetime.now(),
        last_modified=datetime.now(),
    )
    db.session.add(u4)
    db.session.flush()
    u5 = User(
        user_id=5,
        username='bibbby',
        password_digest=b'$2b$12$S6FLSR96c85OBHgRNJx1JuUk.Z4q5Qfu5iwG6vDsBjcZryxUjlu7a',
        email='bib@bibby.com',
        created_at=datetime.now(),
        last_modified=datetime.now(),
    )
    db.session.add(u5)
    db.session.flush()
    u6 = User(
        user_id=6,
        username='bigman',
        password_digest=b'$2b$12$fhmZVqpMnKWLOmuMhUOkseDUNl/ZX236ny/WzckfyDjNe6xjAly3.',
        email='biggestman1@poll.gov',
        created_at=datetime.now(),
        last_modified=datetime.now(),
    )
    db.session.add(u6)
    db.session.flush()
    v1 = Voter(voter_id=1,
              first_name="John",
              middle_name="Jameson",
              last_name="Smith",
              date_of_birth="1987-01-01",
              phone="(319) 335-3305",
              address="1 W Park Rd",
              zip_code="52242-1234",
              state="IA",
              city="Iowa City",
              last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
              zip_last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
              pending=False,
              approved=True,
              approved_date="2023-11-01",
              document1_type='passport',
              document1_info='999ICNTRVL111',
              document2_type='dl',
              document2_info='999ICNDRV111')
    db.session.add(v1)
    v2 = Voter(voter_id=2,
              first_name="Jimmy",
              middle_name="Jason",
              last_name="Jib",
              date_of_birth="1987-01-01",
              phone="(319) 335-3305",
              address="1 W Park Rd",
              zip_code="52242-1234",
              state="IA",
              city="Iowa City",
              last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
              zip_last_modified=now.strftime("%Y/%m/%d %H:%M:%S"),
              pending=True,
              approved=False,
              approved_date=None,
              document1_type='passport',
              document1_info='888ICNTRVL111',
              document2_type='dl',
              document2_info='888ICNDRV111')
    db.session.add(v2)
    db.session.flush()
    new_user_voter_join1 = UsersVotersJoin(voter_id=v1.voter_id, user_id=u2.user_id)
    db.session.add(new_user_voter_join1)
    new_user_voter_join2 = UsersVotersJoin(voter_id=v2.voter_id, user_id=u4.user_id)
    db.session.add(new_user_voter_join2)
    db.session.flush()
    new_user_role_join1 = UsersRolesJoin(user_id=u1.user_id, role_id=1)
    new_user_role_join2 = UsersRolesJoin(user_id=u2.user_id, role_id=3)
    new_user_role_join3 = UsersRolesJoin(user_id=u3.user_id, role_id=2)
    new_user_role_join4 = UsersRolesJoin(user_id=u4.user_id, role_id=3)
    new_user_role_join5 = UsersRolesJoin(user_id=u5.user_id, role_id=2)
    new_user_role_join6 = UsersRolesJoin(user_id=u6.user_id, role_id=2)
    db.session.add(new_user_role_join1)
    db.session.add(new_user_role_join2)
    db.session.add(new_user_role_join3)
    db.session.add(new_user_role_join4)
    db.session.add(new_user_role_join5)
    db.session.add(new_user_role_join6)
    db.session.flush()
    election1 = Election(
        title="Example Election",
        start_datetime="2022-11-08 12:00:00",
        end_datetime="2022-11-08 20:00:00"
    )
    db.session.add(election1)
    db.session.flush()
    precinct1 = Precinct(
        voting_location="University Library",
        state_election_office_contact_address="1 W Park RD Iowa City, IA"
    )
    precinct2 = Precinct(
        voting_location="450 5th Ave SE",
        state_election_office_contact_address="100 1st Ave NE, Cedar Rapids, IA"
    )
    db.session.add(precinct1)
    db.session.add(precinct2)
    db.session.flush()

    race1 = Race(
        name="2022 US Senate - IA"
    )
    race2 = Race(name="2024 US Presidential Election")
    race3 = Race(name="2024 US Congress IA District 1")
    race4 = Race(name="2024 IA State local election 1")
    db.session.add(race1)
    db.session.add(race2)
    db.session.add(race3)
    db.session.add(race4)
    db.session.flush()
    candidate1 = Candidate(
        first_name="Chuck",
        last_name="Grassley",
        party="Republican",
        description="Chuck has been a senator in Iowa for 800 years, he likes the Hawkeyes.",
        incumbent=True
    )
    candidate2 = Candidate(
        first_name="Michael",
        last_name="Franken",
        party="Democrat",
        description="Michael Franken is a pretty good guy, but is a Cyclones fan.",
        incumbent=False
    )
    candidate3 = Candidate(
        first_name="Donald",
        last_name="Trump",
        party="Republican",
        description="Donald believes in building big walls and being tough on China.",
        incumbent=False
    )
    candidate4 = Candidate(
        first_name="Joe",
        last_name="Biden",
        party="Democrat",
        description="Joe wants everyone to get free ice cream and health care.",
        incumbent=True
    )
    candidate5 = Candidate(
        first_name="Steve",
        last_name="King",
        party="Republican",
        description="Steve wants God to run America",
        incumbent=False
    )
    candidate6 = Candidate(
        first_name="Alex",
        last_name="Cortez",
        party="Democrat",
        description="Alex fights for immigrants rights and for all Americans.",
        incumbent=True
    )
    db.session.add(candidate1)
    db.session.add(candidate2)
    db.session.add(candidate3)
    db.session.add(candidate4)
    db.session.add(candidate5)
    db.session.add(candidate6)
    db.session.flush()
    zip1 = ZipCode(
        zip="52242",
        zip_plus_4_start="0000",
        zip_plus_4_end="5000"
    )
    zip2 = ZipCode(
        zip="52242",
        zip_plus_4_start="5001",
        zip_plus_4_end="9999"
    )
    zip3 = ZipCode(
        zip="52402",
        zip_plus_4_start="0000",
        zip_plus_4_end="5000"
    )
    zip4 = ZipCode(
        zip="52402",
        zip_plus_4_start="5001",
        zip_plus_4_end="9999"
    )
    db.session.add(zip1)
    db.session.add(zip2)
    db.session.add(zip3)
    db.session.add(zip4)
    db.session.flush()
    precinct_zip_join1 = PrecinctsZipsJoin(precinct_id=precinct1.precinct_id, zip_id=zip1.zip_id)
    db.session.add(precinct_zip_join1)
    db.session.flush()

    db.session.flush()
    candidate_race_join1 = RacesCandidatesJoin(
        race_id=race1.race_id,
        candidate_id=candidate1.candidate_id
    )
    candidate_race_join2 = RacesCandidatesJoin(
        race_id=race1.race_id,
        candidate_id=candidate2.candidate_id
    )
    candidate_race_join3 = RacesCandidatesJoin(
        race_id=race2.race_id,
        candidate_id=candidate3.candidate_id
    )
    candidate_race_join4 = RacesCandidatesJoin(
        race_id=race2.race_id,
        candidate_id=candidate4.candidate_id
    )
    candidate_race_join5 = RacesCandidatesJoin(
        race_id=race3.race_id,
        candidate_id=candidate5.candidate_id
    )
    candidate_race_join6 = RacesCandidatesJoin(
        race_id=race3.race_id,
        candidate_id=candidate6.candidate_id
    )
    db.session.add(candidate_race_join1)
    db.session.add(candidate_race_join2)
    db.session.add(candidate_race_join3)
    db.session.add(candidate_race_join4)
    db.session.add(candidate_race_join5)
    db.session.add(candidate_race_join6)
    db.session.flush()
    precinct_user_join = PrecinctsUsersJoin(
        precinct_id=precinct1.precinct_id,
        user_id=u3.user_id
    )
    db.session.add(precinct_user_join)
    db.session.flush()
    precinct_user_join = PrecinctsUsersJoin(
        precinct_id=precinct2.precinct_id,
        user_id=u6.user_id
    )
    db.session.add(precinct_user_join)
    db.session.flush()
    ballot1 = Ballot(
        ballot_id=1,
        election_id=1,
        precinct_id=1,
        name='Ballot1',
    )
    db.session.add(ballot1)
    db.session.flush()
    ballot2 = Ballot(
        ballot_id=2,
        election_id=1,
        precinct_id=2,
        name='Ballot2',
    )
    db.session.add(ballot2)
    db.session.flush()
    ballot_race_join1 = BallotsRacesJoin(
        ballot_id=ballot1.ballot_id,
        race_id=race1.race_id
    )
    ballot_race_join2 = BallotsRacesJoin(
        ballot_id=ballot1.ballot_id,
        race_id=race2.race_id
    )
    ballot_race_join3 = BallotsRacesJoin(
        ballot_id=ballot1.ballot_id,
        race_id=race3.race_id
    )
    db.session.add(ballot_race_join1)
    db.session.add(ballot_race_join2)
    db.session.add(ballot_race_join3)
    db.session.commit()
