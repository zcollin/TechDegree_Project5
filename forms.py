from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import (DataRequired, Regexp)

from models import Post


class PostForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    date = DateField("Date", format='%Y-%m-%d', validators=[DataRequired()])
    time_spent = IntegerField("Time Spent (minutes)",
                              validators=[DataRequired()])
    details = TextAreaField("What you Learned", validators=[DataRequired()])
    remember = TextAreaField("Resources to Remember",
                             validators=[DataRequired()])

