from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import InputRequired, Length, Regexp


class ZipForm(FlaskForm):
    zip = StringField(u'Zip Code', description="Enter the main 5-digit zip", validators=[InputRequired(), Length(min=5, max=5, message="Please enter 5 digits"), Regexp(regex=r"^[0-9]{5}$", message="please enter the zip as digits")])
    zip4start = StringField(u'Zip+4 start range', description="Enter the 4-digit start range", validators=[InputRequired(), Length(min=4, max=4, message="Please enter 4 digits"), Regexp(regex=r"^[0-9]{4}$", message="please enter the zip as digits")])
    zip4end = StringField(u'Zip+4 end range', description="Enter the 4-digit end range", validators=[InputRequired(), Length(min=4, max=4, message="Please enter 4 digits"), Regexp(regex=r"^[0-9]{4}$", message="please enter the zip as digits")])
    submit_button = SubmitField(u'Submit')
