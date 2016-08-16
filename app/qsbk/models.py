#coding:utf-8
__author__ = "ila"
from .. import db
class Qsbk(db.Model):
    __tablename__="qsbk"
    id=db.Column(db.Integer,primary_key=True)
    link=db.Column(db.String(64))
    author=db.Column(db.String(64))
    content=db.Column(db.String(300))
    picture=db.Column(db.String(64))
    funny=db.Column(db.String(64))
    reply=db.Column(db.String(64))
    gettime=db.Column(db.DateTime)