# app.py
from flask import Flask  
from flask import Blueprint, request, session, jsonify
from models.chongzhi import *
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

pymysql.install_as_MySQLdb()


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  
@app.route('/exchange', methods=['GET','POST'])
def exchange():
    code = request.args.get('code') #1.用户提交充值码
 
    flag = card.query.filter_by(cardid=code).first() #数据库查询该码
    if flag.cardused=="true": #表示无该充值码或该码已被消费过
            return "yijingyongle"
    elif flag.cardused=="false": 
            flag.cardused="true"
            db.session.commit()
            return "now used"
    else:
            return "404"
@app.route('/exchange2', methods=['GET','POST'])
def exchange2():
    code = request.args.get('code') #1.用户提交充值码
    flag = card.query.filter_by(cardid=code).first() #数据库查询该码
    if flag.cardused=="false": #表示无该充值码或该码已被消费过
            return "yijingyongle"
    else: 
            flag.cardused="false"
            db.session.commit()
            return "now used"
 
if __name__ == '__main__':  
    app.run()   
