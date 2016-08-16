#-*-coding:utf-8-*-
from flask import Flask,request, render_template,flash,session,redirect,url_for
import time,datetime,os
from .forms import RegistrationForm
from ..models import User,books_record
from . import auth
from .. import db,bcrypt,bootstrap
from flask_login import login_required,logout_user



@auth.route("/")
@auth.route("/index")
def index():
    return render_template("auth/index.html",index=u"欢迎来访")

        

@auth.route("/register",methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        bcrypt_password=bcrypt.generate_password_hash(form.password.data)
        user=User(email=form.email.data,
                  username=form.username.data,
                  password=bcrypt_password)
        db.session.add(user)
        db.session.commit()
        flash(u"注册成功，准备登录")
        return redirect(url_for('login.login'))
    return render_template("auth/register.html",form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.login"))

@auth.errorhandler(404)
def page_not_found(e):
    return render_template("auth/404.html")

@auth.errorhandler(500)
def internal_server_error(e):
    return render_template("auth/500.html")