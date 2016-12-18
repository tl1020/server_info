#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'tl'

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 代码如下:
# 当要获取属性值时，用attrib方法。
# 当要获取节点值时，用text方法。
# 当要获取节点名时，用tag方法。

tree = ET.parse('xmltest.xml')
root = tree.getroot()
# print root.tag,root.attrib,root.text

# for child in root:
#     print child.tag,child.attrib
#
# for student in root.findall('list'):
#     no = student.get('id')
#     name = student.find('name').text
#     head = student.find('head').text
#     print (id,head,name)

for i in root.iter()