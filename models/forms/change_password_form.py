from flask_wtf import FlaskForm
from wtforms.fields import PasswordField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Length, Regexp

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField('Current Password', [InputRequired()])
    password = PasswordField(u'New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match'), Length(min=8, message='Password must be at least 8 characters long'), Regexp(regex=r"^[A-Za-z]*(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^*()]).{8,}$", message="Password must meet criteria.")])
    confirm = PasswordField(u'Repeat Password')
    submit_button = SubmitField(u'Update Password')
