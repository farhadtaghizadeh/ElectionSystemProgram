from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField


class VoteForm(FlaskForm):
    submit_button = SubmitField(u'Submit Votes')
