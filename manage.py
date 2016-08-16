#coding:utf-8
from app import app,db

from flask_script import Manager,Server,prompt_bool

manager=Manager(app)
manager.add_command("runserver",Server("127.0.0.1",port=8080))

if  __name__=='__main__':
    manager.run()
