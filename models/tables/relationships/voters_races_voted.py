from configuration.config import db

class VotersRacesVoted(db.Model):
    __tablename__ = "voters_races_voted"
    __table_args__ = {"extend_existing": True}
    submission_id = db.Column(db.Integer, primary_key=True)
    ballot_id = db.Column(db.Integer, nullable=False)
    race_id = db.Column(db.Integer, nullable=False)
    voter_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Ballot "{self.ballot_id}">'
