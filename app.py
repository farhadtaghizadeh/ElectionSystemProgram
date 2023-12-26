from routes import app
from flask import g
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from configuration.config import db, connection_string
from configuration.seed import seed_db
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret key'
app.secret_key = 'development key'
Bootstrap(app)
db.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
migrate = Migrate(app, db)



with app.app_context():
    db.drop_all()
    db.create_all()
    seed_db(db)
    g.app = app

if __name__ == '__main__':
    app.run()
