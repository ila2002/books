#coding:utf-8
__author__ = "ila"
from flask import session,render_template,redirect,url_for,flash,request
from flask_login import login_user
from .forms import  LoginForm
from ..models import  User
from .. import bcrypt,login_manager
from . import login

@login_manager.user_loader
def load_user(id):
    user=User.query.filter_by(id=id).first()
    return user

@login.route("/",methods=["GET","POST"])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        session["username"]=form.loginuser.data
        session["password"]=form.loginpwd.data
        user=User.query.filter_by(username=session.get("username")).first()
        if user and bcrypt.check_password_hash(user.password,session.get("password")):
            flash(u"已登录")
            login_user(user)
            return redirect(request.args.get("next") or url_for("auth.index"))
        else:
            flash(u"密码错误")
    return render_template("login/login.html",form=form,loginuser=session.get("username"),loginpwd=session.get("password"))


