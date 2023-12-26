from configuration.config import db


class Race(db.Model):
    __tablename__ = "races"
    __table_args__ = {'extend_existing': True}
    race_id = db.Column(db.Integer,
                            primary_key=True)
    name = db.Column(db.VARCHAR(255))


    def __repr__(self):
        return f'<Election "{self.race_id}, {self.name}">'
