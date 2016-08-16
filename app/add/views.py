#-*-coding:utf-8-*-
from flask import render_template,flash
from . import add
from .forms import  AddForm
from ..models import books_record
from .. import db
from flask_login import login_required

@add.route('/', methods=['GET', "POST"])
@login_required
def add():
    bookname = None
    author = None
    sortedd = None
    introduction = None
    booklink=None
    commentt = None
    score = None
    state = None

    form = AddForm()
    if form.validate_on_submit():
        bookname = form.bookname.data.replace(" ","")
        author = form.author.data.replace(" ","")
        sortedd = form.sortedd.data.replace(" ","")
        introduction = form.introduction.data
        booklink=form.booklink.data
        commentt = form.commentt.data
        score = form.score.data
        state = form.state.data

        if not bookname and not author:
            flash(u"请重新填写")
        form.bookname.data = ''
        form.author.data = ''
        form.sortedd.data = ''
        form.introduction.data = ''
        form.booklink.data=''
        form.commentt.data = ''
        form.score.data = ''
        form.state.data = ''

        addbooklist = books_record(id='id',
                                   bookname=bookname,
                                   author=author,
                                   sortedd=sortedd,
                                   introduction=introduction.replace('\n','<br />'),
                                   booklink=booklink,
                                   commentt=commentt.replace('\n','<br />'),
                                   score=score,
                                   state=state)
        db.session.add(addbooklist)
        db.session.commit()
        flash("added a book")
    return render_template("add/add.html", form=form, bookname=bookname, author=author, sortedd=sortedd,
                           introduction=introduction, booklink=booklink,commentt=commentt, score=score, state=state)

