from configuration.config import db


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = db.Column(db.Integer,
                        primary_key=True)
    username = db.Column(db.VARCHAR(150),
                         unique=True,
                         nullable=False)
    password_digest = db.Column(db.VARCHAR(150),
                                nullable=False)
    email = db.Column(db.VARCHAR(255),
                      unique=True,
                      nullable=False)
    created_at = db.Column(db.DateTime(),
                           nullable=False)
    last_modified = db.Column(db.DateTime(),
                              nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True

    def get_id(self):
        return str(self.user_id)

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False

    def __repr__(self):
        return f'<User "{self.username}">'
