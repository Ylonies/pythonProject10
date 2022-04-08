from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, DateField, SelectMultipleField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

class JobsForm(FlaskForm):
    job = TextAreaField("Job Title", validators=[DataRequired()])
    team_leader = IntegerField("Team leader ID", validators=[DataRequired()])
    work_size = IntegerField("Work size in hours", validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField("Is job finished?")
    submit = SubmitField('Submit')