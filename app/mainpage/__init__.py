#coding:utf-8
__author__ = "ila"
from flask import Blueprint

mainpage=Blueprint("/mainpage",__name__)

from . import views
