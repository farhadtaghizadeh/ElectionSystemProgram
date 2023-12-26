from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = TextAreaField(u'Username', validators=[DataRequired()])
    password = PasswordField(u'Password', validators=[DataRequired()])

    submit_button = SubmitField(u'Sign In')
