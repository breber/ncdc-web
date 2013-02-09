from wtforms import Form, TextField, PasswordField, BooleanField


class LoginForm(Form):
    """
    A form for users to login.
    """
    username = TextField('Username')
    password = PasswordField('Password')
    remember_me = BooleanField('Remember Me')
