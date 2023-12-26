from configuration.config import db


class UsersRolesJoin(db.Model):
    __tablename__ = "users_roles_join"
    __table_args__ = {'extend_existing': True}
    join_id = db.Column(db.Integer,
                        primary_key=True)
    user_id = db.Column(db.Integer,
                         unique=True,
                         nullable=False)
    role_id = db.Column(db.Integer,
                        unique=False,
                        nullable=False,
                        default=0)

    def __repr__(self):
        return f'<User ID: "{self.user_id} Role ID: {self.role_id}">'
