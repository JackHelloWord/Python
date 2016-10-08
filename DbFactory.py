#!/usr/bin/python
# -*- coding: UTF-8 -*-

' DB '
__author__ = 'Jack Qin'

import sys
sys.path.append("conf")
import config
import sqlite3
import os
import traceback

class DbFactory:
    def __init__(self, show_sql):
        self.__path = config.configs["sqlite"]["sqlite_path"]
        self.__show_sql = show_sql

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def set_sqlite_path(self, sqlite_path):
        self.__path = sqlite_path

    def get_sqlite_path(self):
        return self.__path

    def set_show_sql(self, show_sql):
        self.__show_sql = show_sql

    def get_conn(self, path):
        conn = sqlite3.connect(path)
        #conn.row_factory = self.dict_factory
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
        try:
            if sql is not None and sql != '':
                if data is not None:
                    for d in data:
                        if not isinstance(d, tuple):
                            d = (d,)
                        if self.__show_sql:
                            print('执行sql:[{}],参数:[{}]'.format(sql, d))
                        conn.execute(sql, d)
                    conn.commit()
            else:
                print('the [{}] is empty or equal None!'.format(sql))
            return (1, "normal")
        except Exception as e:
            conn.rollback()
            traceback.print_exc()
            return (-1, traceback.format_exc())

    def fetchall(self, sql, conn):
        if sql is not None and sql != '':
            if self.__show_sql:
                print('执行sql:[{}]'.format(sql))
            cursor = conn.execute(sql)
            r = cursor.fetchall()
            k = []
            for idx, col in enumerate(cursor.description):
                k.append(col[0])
            r.insert(0, k)
            return r
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def fetchone(self, conn, sql, data):
        if sql is not None and sql != '':
            if data is not None:
                d = data
                if not isinstance(data, tuple):
                    d = (data,)
                if self.__show_sql:
                    print('执行sql:[{}],参数:[{}]'.format(sql, data))
                cursor = conn.execute(sql, d)
                r = cursor.fetchall()
                k = []
                for idx, col in enumerate(cursor.description):
                    k.append(col[0])
                r.insert(0, k)
                return r
            else:
                print('the [{}] equal None!'.format(data))
        else:
            print('the [{}] is empty or equal None!'.format(sql))

    def update(self, conn, sql, data):
        try:
            if sql is not None and sql != '':
                if data is not None:
                    if not isinstance(data, tuple):
                        d = (data,)
                    if self.__show_sql:
                        print('执行sql:[{}],参数:[{}]'.format(sql, data))
                    conn.execute(sql, data)
                    conn.commit()
                    print("Total number of rows updated :", conn.total_changes)
                    return (1, conn.total_changes)
            else:
                print('the [{}] is empty or equal None!'.format(sql))
                return (0, 'the [{}] is empty or equal None!'.format(sql))
        except Exception as e:
            conn.rollback()
            traceback.print_exc()
            return (-1, traceback.format_exc())

    def delete(self, conn, sql, data):
        try:
            if sql is not None and sql != '':
                if data is not None:
                    if not isinstance(data, tuple):
                        data = (data,)
                    if self.__show_sql:
                        print('执行sql:[{}],参数:[{}]'.format(sql, data))
                    conn.execute(sql, data)
                    conn.commit()
                    print("Total number of rows deleted :", conn.total_changes)
                    return (1, conn.total_changes)
            else:
                print('the [{}] is empty or equal None!'.format(sql))
                return (0, 'the [{}] is empty or equal None!'.format(sql))
        except Exception as e:
            conn.rollback()
            traceback.print_exc()
            return (-1, traceback.format_exc())

test = DbFactory(True)
#print(test.get_sqlite_path())
conn = test.get_conn(test.get_sqlite_path())
#print(conn)
r = test.fetchone(sql="select * from server where server_name = ? and server_ip = ?", conn=conn, data=("minion134", "192.168.194.134"))
print(r)
#data = [("minion140","192.168.194.140",22,"handhand",-1),]
#r = test.save(sql="insert into server (server_name,server_ip,server_port,password,ifkey) VALUES (?,?,?,?,?)", conn=conn, data=data)
#data = [("minion138", ),]
#r = test.delete(sql="delete from server where server_name = ?", conn=conn, data=data)
#print(r)
#r = test.fetchall(sql="select * from server", conn=conn)
#print(r)
#m = r[0]
#print(r[1][m.index("server_name")])