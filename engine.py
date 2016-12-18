#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'

from sqlalchemy import create_engine,func,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey

engine = create_engine("mysql+mysqldb://root@127.0.0.1:3306/regist?charset=utf8", max_overflow=5, echo=True)
Base = declarative_base()  #生成一个SqlORM 基类

