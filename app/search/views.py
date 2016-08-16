#coding:utf-8
__author__ = "ila"
import math
from flask import render_template,flash,session,request
from flask_login import login_required
from . import search
from .forms import  SearchForm
from .. import db
from ..models import books_record

@search.route("/", methods=["GET", "POST"])
@login_required
def search():
    form = SearchForm()
    page = request.args.get('page', 1, type=int)
    pagination = books_record.query.order_by(books_record.id.desc()).paginate(page, per_page=1, error_out=False)
    #order_by和limit相互抵消，就把排序后的数据只显示一个，起到了limit(1)的效果
    if form.validate_on_submit():
        session['bookname_r'] = form.bookname_s.data.replace(" ", "")
        session['author_r'] = form.author_s.data.replace(" ", "")

        bookname_r = session.get('bookname_r')
        author_r = session.get('author_r')

        if session.get('bookname_r') and session.get('author_r') == '':
            pagination = books_record.query.filter(books_record.bookname.like("%" + bookname_r + "%")).order_by(books_record.id.desc()).paginate(page, per_page=10, error_out=False)

        elif session.get('author_r') and session.get('bookname_r') == '':
            pagination = books_record.query.filter(books_record.author.like("%" + author_r + "%")).order_by(books_record.id.desc()).paginate(page, per_page=10, error_out=False)

        elif session.get('bookname_r') and session.get('author_r'):
            pagination = books_record.query.filter(books_record.bookname.like("%" + bookname_r + "%"),
                                                   books_record.author.like("%" + author_r + "%")).order_by(books_record.id.desc()).paginate(page, per_page=10, error_out=False)
        else:
            flash(u"请输入书名或作者名")

    posts = pagination.items
    total = pagination.total  # 数据总条数
    total = total / 5.0  # 页数的定义
    total = int(math.ceil(total))  #

    form.bookname_s.data = ''
    form.author_s.data = ''
    return render_template("search/search.html", form=form, bookname_s=session.get('bookname_r'),
                           author_s=session.get('author_r'),total=total, posts=posts, pagination=pagination)

