from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length


class PrecinctForm(FlaskForm):
    voting_location = StringField(u'Voting Location', description="Enter the primary location where the election will take place", validators=[InputRequired(), Length(min=0,max=255, message="Please enter an address less than 255 characters")])
    election_office = StringField(u'Election Office Address', description="Enter the contact address for the state office.")
    submit_button = SubmitField(u'Submit')

