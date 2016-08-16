#coding:utf-8
__author__ = "ila"
from flask_wtf import Form
from wtforms import validators,SubmitField,FileField
from wtforms.validators import Required
from flask_pagedown.fields import  PageDownField
from flask_wtf.file import  FileField,FileAllowed,FileRequired
class PageDownForm(Form):
    file=FileField('Presentation in Image Format',
                   validators=[FileRequired(), FileAllowed(['jpg', 'png','txt','rar','zip','doc','xls','gif','pdf'], 'Images only!')])
    body = PageDownField(u"请输入")
    submit=SubmitField('submit')