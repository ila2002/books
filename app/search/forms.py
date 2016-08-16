#coding:utf-8
__author__ = "ila"
from flask_wtf import  Form
from wtforms import StringField,SubmitField

class SearchForm(Form):
    bookname_s=StringField(u"书名")
    author_s=StringField(u"作者")
    submit_s=SubmitField(u"查询")