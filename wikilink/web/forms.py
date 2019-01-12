from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class MainForm(FlaskForm):
    starting_link = StringField('Enter starting wiki link:', validators=[DataRequired()])
    ending_link = StringField('Enter ending wiki link:', validators=[DataRequired()])
    limit = IntegerField('Limit')
    submit = SubmitField('Submit')