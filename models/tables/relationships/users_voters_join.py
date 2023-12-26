from configuration.config import db


class UsersVotersJoin(db.Model):
    __tablename__ = "users_voters_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    voter_id = db.Column(db.Integer,
                         unique=True,
                         nullable=False)
    user_id = db.Column(db.Integer,
                        unique=True,
                        nullable=False,
                        )

    def __repr__(self):
        return f'<Voter ID: "{self.voter_id} User ID: {self.user_id}">'
