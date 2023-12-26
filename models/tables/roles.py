from configuration.config import db


class Role(db.Model):
    __tablename__ = "roles"
    __table_args__ = {'extend_existing': True}
    role_id = db.Column(db.Integer,
                            primary_key=True)
    role_name = db.Column(db.VARCHAR(255))
    role_permissions_level = db.Column(db.Integer)

    def __repr__(self):
        return f'<Role "{self.role_id}, {self.role_name}, {self.role_permissions_level}">'
