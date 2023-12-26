from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, SelectField, BooleanField, DateField, TimeField, IntegerField
from wtforms.validators import DataRequired

class ActivateBallotForm(FlaskForm):
    ballot_id = IntegerField()
    start_date = DateField(u'Start Date', validators=[DataRequired()])
    start_time = TimeField(u'Start Time', validators=[DataRequired()])
    end_date = DateField(u'End Date', validators=[DataRequired()])
    end_time = TimeField(u'End Time', validators=[DataRequired()])
    submit_button = SubmitField(u'Submit')