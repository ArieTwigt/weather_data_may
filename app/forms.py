from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

# form for predictions input
class PredictionRequestForm(FlaskForm):
    country_code = StringField('Country Code')
    city = StringField('City', validators=[DataRequired("Insert a city"),
                                           Length(min=2, max=80)])
    submit = SubmitField('Submit')