from configuration.config import db


class Candidate(db.Model):
    __tablename__ = "candidates"
    __table_args__ = {'extend_existing': True}
    candidate_id = db.Column(db.Integer,
                            primary_key=True)
    first_name = db.Column(db.VARCHAR(255))
    last_name = db.Column(db.VARCHAR(255))
    party = db.Column(db.VARCHAR(255))
    incumbent = db.Column(db.Boolean)
    description = db.Column(db.VARCHAR(255))

    def __repr__(self):
        return f'<Candidate: "{self.first_name} {self.last_name}, Party: {self.party}, Incumbent: {self.incumbent}">'
