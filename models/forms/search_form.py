from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired

class SearchForm(FlaskForm):
    first_name = StringField(u'First Name')
    middle_name = StringField(u'Middle Name')
    last_name = StringField(u'Last Name')
    zip_code = StringField(u'Zip Code')
    polling_station = StringField(u'Polling Station')

    submit_button = SubmitField(u'Search')
