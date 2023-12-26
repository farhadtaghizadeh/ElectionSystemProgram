from configuration.config import db


class PrecinctsZipsJoin(db.Model):
    __tablename__ = "precincts_zips_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    precinct_id = db.Column(db.Integer,
                            unique=False,
                            nullable=False)
    zip_id = db.Column(db.Integer,
                            unique=True,
                            nullable=False)

    def __repr__(self):
        return f'<Precinct ID: "{self.precinct_id} Zip Plus 4: {self.zip_plus_four}">'
