from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, BooleanField
from wtforms.validators import InputRequired


class CandidateForm(FlaskForm):
    first_name = StringField(u'First Name', validators=[InputRequired()])
    last_name = StringField(u'Last Name', validators=[InputRequired()])
    party = StringField(u'Party', validators=[InputRequired()])
    description = StringField(u'Candidate\'s description', validators=[InputRequired()])
    incumbent = BooleanField(u'Incumbent', description="Is this candidate currently elected to the office being contested")
    submit_button = SubmitField(u'Submit')
