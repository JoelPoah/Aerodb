from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField,IntegerField
from wtforms.validators import Length, InputRequired, ValidationError,NumberRange


app = Flask(__name__)
app.config['SECRET_KEY'] = 'apple pie'


class AeroForm(FlaskForm):
    databasenumber = IntegerField("Add number to database",validators=[InputRequired(), NumberRange(0,1)])
    submit = SubmitField("Click to increase number below by 1") 