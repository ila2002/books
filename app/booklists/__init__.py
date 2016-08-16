#coding:utf-8
__author__ = "ila"
from flask import Blueprint

booklists=Blueprint("booklists", __name__, static_folder="static", static_url_path="/booklists")

from . import views,forms