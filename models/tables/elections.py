from configuration.config import db


class Election(db.Model):
    __tablename__ = "elections"
    __table_args__ = {'extend_existing': True}
    election_id = db.Column(db.Integer,
                            primary_key=True)
    title = db.Column(db.VARCHAR(255))
    start_datetime = db.Column(db.DateTime)
    end_datetime = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Election "{self.election_id}, {self.title}, {self.start_datetime}, {self.end_datetime}">'
