from configuration.config import db


class ZipCode(db.Model):
    __tablename__ = "zips"
    __table_args__ = {'extend_existing': True}
    zip_id = db.Column(db.Integer,
                         primary_key=True)
    zip = db.Column(db.VARCHAR(255))
    zip_plus_4_start = db.Column(db.VARCHAR(255))
    zip_plus_4_end = db.Column(db.VARCHAR(255))