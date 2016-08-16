#-*-coding:utf-8-*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown

db = SQLAlchemy()
bcrypt=Bcrypt()
bootstrap=Bootstrap()
login_manager=LoginManager()
pagedown=PageDown()

app=Flask(__name__)
app.config.from_object(config["developmentConfig"])
config["developmentConfig"].init_app(app)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)
bootstrap.init_app(app)
pagedown.init_app(app)

login_manager.login_view="/login"#把login独立出一个模块后，需要修改这里
from .add import add as add_blueprint
app.register_blueprint(add_blueprint,url_prefix="/add")

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint,url_prefix="/auth")

from .mainpage import mainpage as mainpage_blueprint
app.register_blueprint(mainpage_blueprint,url_prefix="/mainpage")

from .login import  login as login_blueprint
app.register_blueprint(login_blueprint,url_prefix="/login")

from .info import info as info_buleprint
app.register_blueprint(info_buleprint,url_prefix="/info")

from .qsbk import qsbk as qsbk_blueprint
app.register_blueprint(qsbk_blueprint,url_prefix="/qsbk")

from .booklists import booklists as booklists_blueprint
app.register_blueprint(booklists_blueprint,url_prefix="/booklists")

from .search import search as search_blueprint
app.register_blueprint(search_blueprint,url_prefix="/search")

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

