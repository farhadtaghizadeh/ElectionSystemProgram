from flask_wtf import FlaskForm
from wtforms.fields import EmailField, StringField, IntegerField, PasswordField, SubmitField, SelectField
from wtforms.validators import Email, InputRequired, EqualTo, Length, Regexp
from models.tables.precincts import Precinct


# precinct_list = Precinct.query.all


class PollingManagerForm(FlaskForm):

    email_address = EmailField(u'Email Address', validators=[Email(message="Please enter a valid email address.")])
    username = StringField(u'Username', validators=[InputRequired()])
    password = PasswordField(u'New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'),
                                               Length(min=8, message='Password must be at least 8 characters long'),
                                               Regexp(
                                                   regex=r"^[A-Za-z]*(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^*()]).{8,}$",
                                                   message="Password must meet criteria.")])
    confirm = PasswordField(u'Repeat Password')
    submit_button = SubmitField(u'Submit')