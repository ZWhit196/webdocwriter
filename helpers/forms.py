from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

from data import Get_user, Is_user # TO ADD


messages = {
    'pass': "The password must be 6 or more characters long, contain 1 number and 1 letter.",
    'bad_pass': "The username/password combination is incorrect.",
    'name': "This name is already in use.",
    'no_user': "No user exists for this name."
}


class Reg_Form(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=32)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if len(self.password.data) < 6 or self.password.data.isalpha() or self.password.data.isdigit():
            self.password.errors.append(messages['pass'])
            return False
        if Is_user(self.name.data):
            self.name.errors.append(messages['name'])
            return False
        return True


class Login_form(FlaskForm):
    name = StringField('Name', [validators.Length(min=4, max=32)])
    password = PasswordField('Password', [validators.DataRequired()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if len(self.password.data) < 6 or self.password.data.isalpha() or self.password.data.isdigit():
            self.password.errors.append(messages['pass'])
            return False
        if not Is_user(self.name.data):
            self.name.errors.append(messages['no_user'])
            return False
        if not Get_user(self.name.data).verify_password(self.password.data):
            self.password.errors.append(messages['bad_pass'])
            return False
        return True


class Password_form(FlaskForm):
    password = PasswordField('New Password', [validators.DataRequired()])

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False
        if len(self.password.data) < 6 or self.password.data.isalpha() or self.password.data.isdigit():
            self.password.errors.append(messages['pass'])
            return False
        return True
