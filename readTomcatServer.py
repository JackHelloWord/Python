#!/usr/bin/python
# -*- coding: UTF-8 -*-

' 读取tomcat的server文件 '
__author__ = 'Jack Qin'

import  xml.dom.minidom
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file='D:/免安装软件/tomcat/conf/server.xml')
Server = tree.getroot()
print(Server.attrib["port"])
print(Server["Service"])




'''
dom = xml.dom.minidom.parse('D:/免安装软件/tomcat/conf/server.xml')

port = []
Server = dom.documentElement
Service = Server.getElementsByTagName("Service")[0]
Connector = Service.getElementsByTagName("Connector")
port.append(Server.getAttribute("port"))
port.append(Connector[0].getAttribute("port"))
port.append(Connector[1].getAttribute("port"))
print(port)
'''