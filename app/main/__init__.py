#coding:utf-8
__author__ = "ila"
from flask import Blueprint

main=Blueprint("main",__name__)

from . import views