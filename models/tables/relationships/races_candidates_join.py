from configuration.config import db


class RacesCandidatesJoin(db.Model):
    __tablename__ = "races_candidates_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    race_id = db.Column(db.Integer,
                            unique=False,
                            nullable=False,
                            )
    candidate_id = db.Column(db.Integer,
                        unique=True,
                        nullable=False)


    def __repr__(self):
        return f'<Race ID: "{self.race_id} Candidate ID: {self.candidate_id}">'
