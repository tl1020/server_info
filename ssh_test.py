#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'
import psutil
from datetime import datetime
import paramiko
import os,sys

# print psutil.users()
# print psutil.boot_time()
# # print datetime.fromtimestamp(psutil.boot_time().strftime("%Y-%m-%d %H:%M:%S"))
# print psutil.disk_io_counters()
# print psutil.net_if_addrs
addr_status1 = psutil.net_if_stats()
print addr_status1
#
# IPADDR = "11.1.0.30"
# username = "root"
#
# paramiko.util.log_to_file('syslogin.log')
#
# ssh = paramiko.SSHClient()
# ssh.load_system_host_keys()
# privateKey = os.path.expanduser('~/.ssh/id_rsa')    #定义私钥存放路径
# key = paramiko.RSAKey.from_private_key_file(privateKey) #创建私钥对象Key
#
# ssh.connect(hostname=IPADDR,username=username,pkey=key)
#
# stdin,stdout,stderr = ssh.exec_command('ifconfig')
#
# print stdout.read()
#
# ssh.close()
