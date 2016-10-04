#!/usr/bin/python
# -*- coding: UTF-8 -*-

' 测试sqlite '
__author__ = 'Jack Qin'

import sys
sys.path.append("conf")
import config
import sqlite3
import os

class DbFactory:
    def __init__(self, show_sql):
        self.__path = config.configs["sqlite"]["sqlite_path"]
        self.__show_sql = show_sql

    def set_sqlite_path(self, sqlite_path):
        self.__path = sqlite_path

    def get_sqlite_path(self):
        return self.__path

    def set_show_sql(self, show_sql):
        self.__show_sql = show_sql

    def get_conn(self, path):
        conn = sqlite3.connect(path)
        if os.path.exists(path) and os.path.isfile(path):
            print('硬盘上面:[{}]'.format(path))
            return conn
        else:
            conn = None
            print('内存上面:[:memory:]')
            return sqlite3.connect(':memory:')

    def get_cursor(self, conn):
        if conn is not None:
            return conn.cursor()
        else:
            return get_conn('').cursor()

    def close(self, cc):
        try:
            if cc is not None:
                cc.close()
        finally:
            if cc is not None:
                cc.close()

    def save(self, sql, data, conn):
        if sql is not None and sql != '':
            if data is not None:
                for d in data:
                    if self.__show_sql:
                        print('执行sql:[{}],参数:[{}]'.format(sql, d))
                    conn.execute(sql, d)
                    conn.commit()
                    self.close(conn)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchall(self, sql, conn):
        if sql is not None and sql != '':
            if self.__show_sql:
                print('执行sql:[{}]'.format(sql))
            cursor = conn.execute(sql)
            print(cursor)
            self.close(conn)
            self.close(cursor)
        else:
            print('the [{}] is empty or equal None!'.format(sql))

test = DbFactory(True)
#print(test.get_sqlite_path())
conn = test.get_conn(test.get_sqlite_path())
print(conn)
#test.fetchall(sql="select * from server", conn=conn)