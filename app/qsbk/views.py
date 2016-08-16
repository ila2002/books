#coding:utf-8
__author__ = "ila"
import datetime,time,math
from flask import request,render_template,flash
from flask_login import login_required
from . import qsbk
from .models import Qsbk
from .. import bootstrap

@qsbk.route("/",methods=["GET","POST"])
@login_required
def qsbk():
    form=request.form
    if request.method=='post':
        if form.get("update")==u"更新":
            if execfile("qsbk_update.py"):
                flash(qsbk_up+u"已刷新")
    date1=datetime.date.today()
    datetime0=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    datetime1=datetime.datetime.strptime(str(date1)+" 00:00:00",'%Y-%m-%d %H:%M:%S')
    datetime2=datetime.datetime.strptime(datetime0,'%Y-%m-%d %H:%M:%S')
    page=request.args.get("page",1,type=int)
    pagination=Qsbk.query.filter(Qsbk.gettime.between(datetime1,datetime2)).group_by('qsbk.link').order_by('id desc').paginate(page,per_page=5,error_out=False)
    posts=pagination.items
    total=pagination.total
    total=total/5.0
    total=int(math.ceil(total))
    return render_template("qsbk/qsbk.html",total=total,posts=posts,pagination=pagination)