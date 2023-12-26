from datetime import datetime

from configuration.config import db

class Ballot(db.Model):
    __tablename__ = "ballots"
    __table_args__ = {"extend_existing": True}
    ballot_id = db.Column(db.Integer, primary_key=True)
    election_id = db.Column(db.Integer)
    precinct_id = db.Column(db.Integer)
    name = db.Column(db.VARCHAR(255), nullable=False)
    activated = db.Column(db.Boolean, nullable=False, default=False)
    start_datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Ballot "{self.ballot_id}, {self.name}">'
