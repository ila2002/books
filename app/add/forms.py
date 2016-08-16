#-*-coding:utf-8-*-
from flask_wtf import Form
from wtforms import StringField,TextAreaField,RadioField,SelectField,SubmitField
from wtforms.validators  import Required
class AddForm(Form):
  bookname=StringField(u'书名',validators=[Required()])
  author=StringField(u'作者',validators=[Required()])
  sortedd=StringField(u'分类',validators=[Required()])
  introduction=TextAreaField(u'简介')
  booklink = StringField(u'书链')
  commentt=TextAreaField(u'书评')
  score=SelectField(u'评分', choices=[
        (u'★', u'★'), (u'★★', u'★★'),(u'★★★', u'★★★'),(u'☆', u'☆')], default=u'☆')
  state=SelectField(u'状态', choices=[
        (u'追看', u'追看'), (u'断更', u'断更'),(u'看完',u'看完'),(u'弃书',u'弃书')], default=u'追看')
  submit=SubmitField(u'提交')