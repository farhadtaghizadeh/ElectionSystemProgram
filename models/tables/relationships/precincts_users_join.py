from configuration.config import db


class PrecinctsUsersJoin(db.Model):
    __tablename__ = "precincts_users_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    precinct_id = db.Column(db.Integer,
                            unique=True,
                            nullable=False)
    user_id = db.Column(db.Integer,
                        unique=False,
                        nullable=False,
                        )

    def __repr__(self):
        return f'<Precinct ID: "{self.precinct_id} Polling Manager\'s ID: {self.user_id}">'
