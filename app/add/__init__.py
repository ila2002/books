#-*-coding:utf-8-*-
from flask import Blueprint

add=Blueprint("add",__name__,static_folder="static",static_url_path="/all")

from . import views,forms