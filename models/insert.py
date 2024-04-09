from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 不加以下两行可能会报错  RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set.
app_ctx = app.app_context()     
app_ctx.push()


class BaseConfig():
    DEBUG = True
    # 获取项目目录
    APP_PATH = os.path.dirname(__file__)

    # mysql数据库url
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@192.168.133.128:3306/flask1227?charset=utf8"


app.config.from_object(BaseConfig)

# 创建数据库连接，管理项目
db = SQLAlchemy(app)

class card(db.Model):  #模型类继承db.Model
    cardid = db.Column(db.INTEGER, primary_key=True)
    cardused = db.Column(db.String(50))
    # desc = db.Column(db.String(40))   # 增加一个字段 run后没有加入表中，要先删除表，再run,然后刷新表


if __name__ == '__main__':
    # 删除所有表
    # db.drop_all()
    #db.create_all()   # 创建所有的表
    card3 = card(cardid='1', cardused='false')
    db.session.add(card3)
    db.session.commit()
