from configuration.config import db


class BallotsRacesJoin(db.Model):
    __tablename__ = "ballots_races_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    ballot_id = db.Column(db.Integer,
                            unique=False,
                            nullable=False)
    race_id = db.Column(db.Integer,
                        unique=False,
                        nullable=False,
                        )

    def __repr__(self):
        return f'<Election ID: "{self.ballot_id} Race ID: {self.race_id}">'
