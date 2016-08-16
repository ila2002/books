#coding:utf-8
__author__ = "ila"
from flask import Blueprint
search=Blueprint("search",__name__,static_folder='static',static_url_path="/search")

from . import views,forms