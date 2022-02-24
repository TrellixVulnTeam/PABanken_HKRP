# from wtforms.validators import Required
from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators
from wtforms.fields import IntegerField, SelectField, BooleanField, DateTimeField, SubmitField

class PersonEditForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    city = StringField("city",[validators.Length(min=5, max=30)])
    postalcode = IntegerField("postalcode",[validators.NumberRange(10000,99999)])
    pwd = StringField("pwd",[validators.Length(min=5, max=30), validators.EqualTo('pwdagain') ])
    #["kalle", "lisa" ]
    pwdagain = StringField("pwdagain",[validators.Length(min=5, max=30)])
    position = SelectField("Spelar position", choices=[('g', 'Goalie'), ('d', 'Defence'), ('f', 'Forward')])    


class PersonNewForm(FlaskForm):
    name = StringField("name",[validators.Length(min=3, max=80, message="Skriv in mellan 2 och 80 tecken")])
    city = StringField("city",[validators.Length(min=5, max=30)])
    postalcode = IntegerField("postalcode",[validators.NumberRange(10000,99999)])
    position = SelectField("Spelar position", choices=[('g', 'Goalie'), ('d', 'Defence'), ('f', 'Forward')])    


class UserRegistrationForm(FlaskForm):
    email = StringField("Epost",[validators.Email()])
    firstname = StringField("Förnamn",[validators.Length(min=5, max=40)])
    lastname = StringField("Efternamn",[validators.Length(min=5, max=40)])
    
    val = []
    val.append(validators.Length(min=5, max=30))
    val.append(validators.EqualTo('pwdagain'))
    pwd = StringField("pwd",val)

    pwdagain = StringField("pwdagain",[validators.Length(min=5, max=30)])
    updates = BooleanField("Send me important updates")

class TransactionNewForm(FlaskForm):
    AccountID = IntegerField("Account ID",[validators.NumberRange(1,99999)])
    PersonId = IntegerField("Person ID",[validators.NumberRange(1,99999)])
    Amount = IntegerField("Amount",[validators.NumberRange(-999999,999999)])
    Datum = DateTimeField("Datum")
   