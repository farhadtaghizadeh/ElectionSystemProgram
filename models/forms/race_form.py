from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired


class RaceForm(FlaskForm):
    name = StringField(u'Name', validators=[InputRequired()])
    submit_button = SubmitField(u'Submit')
