#coding:utf-8
__author__ = "ila"
from flask import render_template
from . import mainpage

@mainpage.route("/")
def index():
    return render_template("mainpage/index.html")
