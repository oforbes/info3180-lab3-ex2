from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired,Email,Required
from wtforms.fields import TextField, TextAreaField, SubmitField



class ContactForm(FlaskForm):
    name = TextField("Name", validators=[Required("Please enter your name.")])
    email = StringField('Email', validators=[InputRequired("Please enter your email.")])
    subject = StringField('Subject', validators=[InputRequired("Please enter a subject")])
    message = StringField('Message', validators=[InputRequired("Please enter your message")])
    Submit = SubmitField("Submit")