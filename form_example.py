from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired


class CityForm(FlaskForm):
    city = SelectField('Select your city', validators=[
                       DataRequired()], choices=[("value1", "Label1"), ("value2", "Label2")])
    submit = SubmitField('Submit')
