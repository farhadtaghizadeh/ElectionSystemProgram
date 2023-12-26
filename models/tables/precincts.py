from configuration.config import db


class Precinct(db.Model):
    __tablename__ = "precincts"
    __table_args__ = {'extend_existing': True}
    precinct_id = db.Column(db.Integer,
                            primary_key=True)
    voting_location = db.Column(db.VARCHAR(255))
    state_election_office_contact_address = db.Column(db.VARCHAR(255))

    def __repr__(self):
        return f'<Precinct "{self.precinct_id}, {self.voting_location}">'
