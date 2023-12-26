from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired

class BallotForm(FlaskForm):
    name = StringField(u'Name', validators=[InputRequired()])
    elections = SelectField(u'Election', choices=[], validators=[InputRequired()])
    precincts = SelectField(u'Precinct', choices=[], validators=[InputRequired()])
    submit_button = SubmitField(u'Submit')