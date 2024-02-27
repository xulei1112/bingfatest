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
    if not flag: #表示无该充值码或该码已被消费过
            return "helleo"
    else: 
            return "sdasdasd"
 
if __name__ == '__main__':  
    app.run()   
