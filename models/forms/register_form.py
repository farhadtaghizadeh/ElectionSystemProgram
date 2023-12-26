from flask_wtf import FlaskForm
from wtforms.fields import EmailField, StringField, DateField, PasswordField, SubmitField, SelectField
from wtforms.validators import Email, InputRequired, EqualTo, Length, Regexp


states = [
    ('AK', 'Alaska'),
    ('AL', 'Alabama'),
    ('AR', 'Arkansas'),
    ('AZ', 'Arizona'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DC', 'District of Columbia'),
    ('DE', 'Delaware'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('IA', 'Iowa'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('MA', 'Massachusetts'),
    ('MD', 'Maryland'),
    ('ME', 'Maine'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MO', 'Missouri'),
    ('MS', 'Mississippi'),
    ('MT', 'Montana'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('NE', 'Nebraska'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NV', 'Nevada'),
    ('NY', 'New York'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('Pa', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VA', 'Virginia'),
    ('VT', 'Vermont'),
    ('WA', 'Washington'),
    ('WI', 'Wisconsin'),
    ('WV', 'West Virginia'),
    ('WY', 'Wyoming')
]

class RegisterForm(FlaskForm):
    email_address = EmailField(u'Email Address', validators=[Email(message="Please enter a valid email address.")])
    username = StringField(u'Username', validators=[InputRequired()])
    password = PasswordField(u'New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, message='Password must be at least 8 characters long'), Regexp(regex=r"^[A-Za-z]*(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^*()]).{8,}$", message="Password must meet criteria.")])
    confirm = PasswordField(u'Repeat Password')
    first_name = StringField(u'First Name', validators=[InputRequired()])
    middle_name = StringField(u'Middle Name', validators=[InputRequired()])
    last_name = StringField(u'Last Name', validators=[InputRequired()])
    phone_number = StringField(u'Phone Number', validators=[InputRequired()])
    date_of_birth = DateField(u'Birthday', validators=[InputRequired()])
    address = StringField(u'Street Address', validators=[InputRequired()])
    address2 = StringField(u'Apt/Unit #')
    city = StringField(u'City', validators=[InputRequired()])
    state = SelectField(u'State', choices=states, validators=[InputRequired()])
    zip_code = StringField(u'Zip Code', validators=[InputRequired(), Length(min=10,max=10, message="Please enter the full zip+4 address, including the dash"), Regexp(regex=r"^[0-9]{5}(?:-[0-9]{4})?$", message="please enter the zip as digits in the format xxxxx-xxxx")])
    gov_id_1_type = SelectField(u'First ID Type', choices=[('dl', "Driver's License"), ('passport', "Passport"), ('sid', "State ID")])
    gov_id_1 = StringField(u'First Government ID', validators=[InputRequired()])
    gov_id_2_type = SelectField(u'Second ID Type', choices=[('dl', "Driver's License"), ('passport', "Passport"), ('sid', "State ID")])
    gov_id_2 = StringField(u'Second Government ID', validators=[InputRequired()])
    submit_button = SubmitField(u'Submit')
