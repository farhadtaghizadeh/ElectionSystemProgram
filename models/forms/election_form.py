from flask_wtf import FlaskForm
from wtforms.fields import StringField, DateField, TimeField, SubmitField
from wtforms.validators import InputRequired


class ElectionForm(FlaskForm):
    title = StringField(u'Title', validators=[InputRequired()])
    start_date = StringField(u'Start Date', validators=[InputRequired()])
    start_time = StringField(u'Start Time', validators=[InputRequired()])
    end_date = StringField(u'End Date', validators=[InputRequired()])
    end_time = StringField(u'End Time', validators=[InputRequired()])
    submit_button = SubmitField(u'Submit')
