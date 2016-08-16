#coding:utf-8
__author__ = "ila"
from flask import Blueprint

info=Blueprint("info",__name__)

from . import views