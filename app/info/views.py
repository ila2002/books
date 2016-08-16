#coding:utf-8
__author__ = "ila"
from flask import request,render_template,Response
from . import info
import socket

@info.route("/")
def info():
    ip=request.remote_addr
    if ip:
        pcname=socket.gethostbyaddr(ip)[0]
    else:
        pcname=None
    return render_template("info/info.html",ip=ip,pcname=pcname)
