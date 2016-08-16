#coding:utf-8
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get("SECRET_KEY") or "whatthefuck?"
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    #UPLOAD_FOLDER= "static/upload"

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql://root:@127.0.0.1:3306/books?charset=utf8"

config={
    'developmentConfig':DevelopmentConfig,
    'default':DevelopmentConfig
}
