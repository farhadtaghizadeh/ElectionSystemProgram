from configuration.config import db

class Vote(db.Model):
    __tablename__ = "votes"
    __table_args__ = {"extend_existing": True}
    vote_id = db.Column(db.Integer, primary_key=True)
    ballot_id = db.Column(db.Integer, nullable=False)
    election_id = db.Column(db.Integer, nullable=False)
    race_id = db.Column(db.Integer, nullable=False)
    candidate_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Vote "{self.vote_id}">'
