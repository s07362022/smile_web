from flask_wtf import Form
#from wtforms import TextField, BooleanField, PasswordField, TextAreaField, validators
from wtforms import StringField, SubmitField, validators, PasswordField
from wtforms.fields.html5 import EmailField
from model import UserReister
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
class FormRegister(FlaskForm):

    # id =  0
    username = StringField('姓名', validators=[
        validators.DataRequired(),
        validators.Length(2,30)
    ])
    id = StringField('身分證', validators=[
        validators.DataRequired(),
        validators.Length(10,30)
    ])
    hpname = StringField('醫院', validators=[
        validators.DataRequired(),
        validators.Length(1,30)
    ])
    submit = SubmitField('退出研究')
    # email = EmailField('Email', validators=[
    #     validators.DataRequired(),
    #     validators.Length(1, 50),
    #     validators.Email()
    # ])
    # password = PasswordField('密碼', validators=[
    #     validators.DataRequired(),
    #     validators.Length(5, 20),
    #     validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    # ])
    # password2 = PasswordField('密碼確認', validators=[
    #     validators.DataRequired()
    # ])
    

    # def validate_email(self, field):
    #     if UserReister.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email 已經被使用')

    # def validate_username(self, field):
    #     if UserReister.query.filter_by(username=field.data).first():
    #         raise  ValidationError('UserName 已經被使用')