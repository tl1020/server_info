#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'

from sqlalchemy import create_engine,func,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from init_db import *


engine = create_engine("mysql+mysqldb://root@127.0.0.1:3306/regist?charset=utf8", max_overflow=5, echo=True)
Base = declarative_base()  #生成一个SqlORM 基类

metadata = MetaData()

Session = sessionmaker(bind=engine)  #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session()


for i in session.query(server_type).order_by(server_type.id).all():
    print i.id
1