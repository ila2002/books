#coding:utf-8
__author__ = "ila"
from flask import flash,request,redirect,url_for
from werkzeug import secure_filename
import os
from flask_login  import current_user,login_required
from . import main
from .. import pagedown,app
from .forms import PageDownForm
from flask import render_template
app.config['UPLOAD_FOLDER']="upload"

@login_required
@main.route("/",methods=["GET","POST"])
def main():
    filen=None
    form =PageDownForm()
    if form.validate_on_submit():
        text=form.body.data
        file=form.file.data
        filename=secure_filename(file.filename)

        if current_user.is_authenticated:
            user_folder = current_user.username
            path1 = os.path.abspath(os.curdir) + "\\" + app.config['UPLOAD_FOLDER'] + "\\" + user_folder
            if os.path.exists(path1):
                pass
            else:
                os.mkdir(path1)
            file.save(os.path.join(app.config['UPLOAD_FOLDER']+"/"+user_folder ,filename))
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'] , filename))
        return filename+r" 已上传"

    return render_template('index.html', form=form )
