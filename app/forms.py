from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired,  Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], description="Please enter your full name")
    email = StringField('E-mail', validators=[DataRequired(),Email()], description="Please enter your e-mail address")
    subject = StringField('Subject', validators=[DataRequired()], description="Please enter the subject for your message")
    message = TextAreaField('Message', validators=[DataRequired()], description="Please enter the message you would like to send")
