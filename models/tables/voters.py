from configuration.config import db


class Voter(db.Model):
    __tablename__ = "voters"
    __table_args__ = {'extend_existing': True}
    voter_id = db.Column(db.Integer,
                         primary_key=True)
    first_name = db.Column(db.VARCHAR(255))
    middle_name = db.Column(db.VARCHAR(255))
    last_name = db.Column(db.VARCHAR(255))
    date_of_birth = db.Column(db.Date)
    phone = db.Column(db.VARCHAR(255))
    address = db.Column(db.VARCHAR(255))
    address_2 = db.Column(db.VARCHAR(255))
    city = db.Column(db.VARCHAR(255))
    state = db.Column(db.VARCHAR(255))
    zip_code = db.Column(db.VARCHAR(255))
    last_modified = db.Column(db.Date)
    zip_last_modified = db.Column(db.DateTime)
    document1_type = db.Column(db.Text)
    document1_info = db.Column(db.Text)
    document2_type = db.Column(db.Text)
    document2_info = db.Column(db.Text)
    pending = db.Column(db.Boolean, nullable=False)
    approved = db.Column(db.Boolean)
    approved_date = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Voter "{self.last_name}, {self.first_name}, {self.middle_name}">'
