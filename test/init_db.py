#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'

from sqlalchemy import create_engine,func,and_,or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,backref
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from engine import engine

engine = create_engine("mysql+mysqldb://root@127.0.0.1:3306/server_info?charset=utf8", max_overflow=5, echo=True)
Base = declarative_base()  #生成一个SqlORM 基类

Session = sessionmaker(bind=engine)  #创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session()

metadata = MetaData()

class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    cms_id = Column(String(20))
    ip = Column(String(15),nullable=False)
    user = Column(String(20))
    password = Column(String(20))
    port = Column(Integer,default=22)
    server_type = Column(String(20))
    is_oracle = Column(Integer)
    note = Column(String(255))
#    platform = relationship("platform", backref="server")

#各模块类型，如接入、分发
class server_type(Base):
    __tablename__ = 'server_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    note = Column(String(255))

class oracle_info(Base):
    __tablename__ = 'oracle_info'
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer,nullable=False)
    service_name = Column(String(10))
    SID = Column(String(10))
    port = Column(Integer,default=1521)
    logon_name = Column(String(20))
    password = Column(String(20))
    note = Column(String(255))

class mysql_info(Base):
    __tablename__ = 'mysql_info'
    id = Column(Integer, primary_key=True)
    server_id = Column(Integer,nullable=False)
    db_name = Column(String(10))
    port = Column(Integer,default=3306)
    logon_name = Column(String(20))
    password = Column(String(20))
    note = Column(String(255))

class Platform(Base):
    __tablename__ = 'platform'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    cms_id = Column(String(20),unique=True,nullable=False)
    parent_id = Column(String(20))
    note = Column(String(255))
#    server = relationship("Server",backref="platform")

Base.metadata.create_all(engine)   #创建所有表结构

session.add_all([
    server_type(id=1,name='中心管理服务器'),
    server_type(id=2,name='数据库服务器'),
    server_type(id=3,name='接入服务器'),
    server_type(id=4,name='分发服务器'),
    server_type(id=5,name='存储服务器'),
    server_type(id=6,name='目录服务器'),
    server_type(id=7,name='目录服务器数据库'),
    server_type(id=8,name='日志服务器'),
    server_type(id=9,name='日志服务器数据库'),
    server_type(id=10,name='网管服务器'),
    server_type(id=11,name='网管服务器数据库'),
    server_type(id=12,name='诊断服务器'),
    server_type(id=13,name='ftp服务器'),
    server_type(id=14,name='卡口中心服务器'),
    server_type(id=15,name='卡口数据库服务器'),
    server_type(id=16,name='卡口接入服务器'),
    server_type(id=17,name='上级信令网关'),
    server_type(id=18,name='上级媒体网关'),
    server_type(id=19,name='下级信令网关'),
    server_type(id=20,name='下级媒体网关'),
    server_type(id=21,name='视频复用服务器'),
    server_type(id=22,name='摘要服务器'),
    server_type(id=23,name='智能分析服务器'),
    server_type(id=24,name='人脸识别服务器'),
    server_type(id=25,name='MSP服务器'),
    server_type(id=26,name='手机转码服务器')
])
session.commit()

#删除user表中，id大于2的字段
#session.query(User).filter(User.id > 2).delete()
#session.commit()
#user表里的id等于2的字段修改为id=6
#session.query(User).filter(User.id == 2).update({'id' : 6})
#session.commit()