from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__="login"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100))
    password=db.Column(db.String(100))
    email=db.Column(db.String(100))
    Invite_Code=db.Column(db.String(255))
    done1=db.Column(db.String(100))


class books_record(db.Model):
    __tablename__="ebook"
    id=db.Column(db.Integer,primary_key=True)
    bookname=db.Column(db.String(64))
    author=db.Column(db.String(64))
    sortedd=db.Column(db.String(64))
    introduction=db.Column(db.String(600))
    booklink = db.Column(db.String(255))
    commentt=db.Column(db.String(600))
    score=db.Column(db.String(64))
    state=db.Column(db.String(64))

