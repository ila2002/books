#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,RadioField,SelectField,BooleanField,validators
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(Form):
    email=StringField(u'邮箱地址:',validators=[Required(),Length(1,64),Email()])

    username=StringField(u'用户名:',validators=[
        Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,
                                       'Usernames must have only letters,'
                                       'numbers,dots or underscores')])

    password=PasswordField(u'密码:',validators=[
        Required(),EqualTo('password2',message='passwords must match.')])

    password2=PasswordField(u'确认密码:',validators=[Required()])

    submit=SubmitField(u'注册:')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
    def validte_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')
