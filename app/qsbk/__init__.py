#coding:utf-8
__author__ = "ila"
from flask import Blueprint
qsbk=Blueprint("qsbk",__name__,static_folder='static',static_url_path="/qsbk")

from . import views,models