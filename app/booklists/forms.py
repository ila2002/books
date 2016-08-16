from flask_wtf import Form
from wtforms import validators,TextField,TextAreaField,SelectField,SubmitField,StringField,RadioField

class EditForm(Form):
    bookname = StringField(u'书名')
    author = StringField(u'作者')
    sortedd = StringField(u'分类')
    introduction = TextAreaField(u'简介')
    booklink = StringField(u'书链')
    commentt = TextAreaField(u'书评')
    score = RadioField(u'评分', choices=[
        (u'★★★', u'★★★'), (u'★★', u'★★'), (u'★', u'★'), (u'☆', u'☆')], default=u'☆')
    state = SelectField(u'状态', choices=[
        (u'追', u'追'), (u'断', u'断'), (u'完', u'完'), (u'弃', u'弃')], default=u'追')
    submit = SubmitField(u'修改')