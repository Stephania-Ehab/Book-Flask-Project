from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    title = StringField("Tiltle", validators=[DataRequired(), Length(2, 40)])
    description = StringField("Description")
    image= FileField("Cover Image") 
    page= IntegerField ('Number of Pages', validators=[DataRequired()])
    submit = SubmitField("submit")
