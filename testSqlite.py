#!/usr/bin/python
# -*- coding: UTF-8 -*-

' 测试sqlite '
__author__ = 'Jack Qin'

sys.path.append("conf")
import config
import sqlite3

conn = sqlite3.connect()
cursor = conn.cursor()

class