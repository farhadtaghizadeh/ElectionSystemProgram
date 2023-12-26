from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp
from models.helpers.getters import get_poll_managers


class AssignPollManager(FlaskForm):
    polling_manager = StringField(u'Username', validators=[InputRequired()], description="enter the username of the polling manager")
    submit_button = SubmitField(u'Submit')