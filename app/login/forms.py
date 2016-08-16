#coding:utf-8
__author__ = "ila"
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required

class LoginForm(Form):
    loginuser=StringField(u'用户名',validators=[Required()])
    loginpwd=PasswordField(u'密码',validators=[Required()])
    loginsubmit=SubmitField(u"登录")