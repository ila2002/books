# coding:utf-8
__author__ = "ila"
from flask import render_template,flash,request,redirect,url_for
from . import booklists
from flask_login import login_required
from ..models import books_record
import math
from.forms import EditForm
from .. import db

@booklists.route('/')
@login_required
def booklist():
    page = request.args.get('page', 1, type=int)
    pagination = books_record.query.order_by(books_record.id.desc()).paginate(page, per_page=10, error_out=False)
    posts = pagination.items
    total = pagination.total  # 数据总条数
    total = total / 5.0  # 页数的定义
    total = int(math.ceil(total))  #
    return render_template('booklists/booklists.html', total=total, posts=posts, pagination=pagination)

    # alldata=books_record.query.all()
    # return render_template("all/all.html",alll=alldata)



@booklists.route('/<bk>', methods=['GET', "POST"])
@login_required
def bk(bk):
    bksdata = books_record.query.filter_by(id=bk).first()
    if request.form.get("submit")==u"修改":
        return redirect(url_for("booklists.editor",bk_id=bk))
        #按钮按下后跳转到修改页面，并把参数传递给编辑函数

    return render_template("booklists/bk.html",bksdata=bksdata)



@booklists.route("/edit/<bk_id>",methods=["GET","POST"])
@login_required
def editor(bk_id):
    bookname = None
    author = None
    sortedd = None

    score = None
    state = None
    booklink = None

    commentt = None
    introduction = None
    editdata = books_record.query.filter_by(id=int(bk_id)).first()#接收到传递过来的book.id后开始查询
    form = EditForm()
    if form.validate_on_submit():
        bookname=form.bookname.data
        author=form.author.data
        sortedd=form.sortedd.data
        introduction=form.introduction.data
        booklink=form.booklink.data
        commentt=form.commentt.data
        score=form.score.data
        state=form.state.data
        books_record.query.filter_by(id=editdata.id).update(dict(bookname=bookname,
                                                                author=author,
                                                                sortedd=sortedd,
                                                                score=score,
                                                                state=state,
                                                                booklink=booklink,
                                                                commentt=commentt,
                                                                introduction=introduction))
        db.session.commit()
        return redirect(url_for("booklists.bk",bk=bk_id))
        flash("update is ok")
    #下面把上面数据库查询得到的数据传递给form，方便后面的编辑
    form.bookname.data = editdata.bookname
    form.author.data = editdata.author
    form.sortedd.data = editdata.sortedd
    form.introduction.data = editdata.introduction
    form.booklink.data = editdata.booklink
    form.commentt.data = editdata.commentt
    form.score.data = editdata.score
    form.state.data = editdata.state
    return render_template("booklists/editor.html",
                           form=form,
                           bookname=bookname,
                           author=author,
                           sortedd=sortedd,
                           introduction=introduction,
                           booklink=booklink,
                           commentt=commentt,
                           score=score,
                           state=state
                           )