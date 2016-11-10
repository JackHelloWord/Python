#!/usr/bin/python
# -*- coding: UTF-8 -*-

' INSTALLER '
__author__ = 'Jack Qin'

import sys
sys.path.append("conf")
import DbFactory

class InstallerFactory:
    def __init__(self):
        pass

    def save_install(self,
                 path,
                 user_id,
                 server_id,
                 ifinstall
                 ):
        install_data = (path,
                    user_id,
                    server_id,
                    ifinstall)
        sql = ("install INTO install ("
               "path,"
               "user_id,"
               "server_id,"
               "ifinstall"
               ") "
               "VALUES(?,?,?,?)"
               )

        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.save(sql=sql,conn=conn, data=install_data)
        db.close(conn)

        return r

    def fetchall(self):
        sql = "select * from install"
        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.fetchall(sql=sql, conn=conn)
        db.close(conn)

        return r

    def fetchone(self, paramaters, conditions):
        data = ()
        sql = "select "
        if not isinstance(paramaters, tuple):
            paramaters = (paramaters, )
        for i in range(len(paramaters)):
            temp = ", " if i != len(paramaters) - 1 else " "
            sql = sql + str(paramaters[i]) + temp

        sql = sql + "from install "

        if len(conditions) != 0:
            if not isinstance(conditions, dict):
                return(0, "conditions is not a dict")
            tempd = []
            sql = sql + "where "
            kv = list(conditions.items())
            for i in range(len(kv)):
                temp = ", " if i != len(kv) - 1 else " "
                sql = sql + str(kv[i][0]) + " = ?" + temp
                tempd.append(kv[i][1])
            data = tuple(tempd)

        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.fetchone(sql=sql, conn=conn, data=data)
        db.close(conn)

        return r

    def delete(self, conditions):
        data = []
        sql = "DELETE FROM install "

        if len(conditions) != 0:
            if not isinstance(conditions, dict):
                return(0, "conditions is not a dict")
            tempd = []
            sql = sql + "where "
            kv = list(conditions.items())
            for i in range(len(kv)):
                temp = ", " if i != len(kv) - 1 else " "
                sql = sql + str(kv[i][0]) + " = ?" + temp
                tempd.append(kv[i][1])
            data = tuple(tempd)

        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.delete(sql=sql, conn=conn, data=data)
        db.close(conn)

        return r

    def update(self, paramaters, conditions):
        data = ()
        tempd = []
        sql = "UPDATE FROM install SET "
        if not isinstance(paramaters, dict):
            return (0, "paramaters is not a dict")
        kv = list(conditions.items())
        for i in range(len(kv)):
            temp = ", " if i != len(paramaters) - 1 else " "
            sql = sql + str(kv[i][0]) + " = ?" + temp
            tempd.append(kv[i][1])

        if len(conditions) != 0:
            if not isinstance(conditions, dict):
                return(0, "conditions is not a dict")
            sql = sql + "where "
            kv = list(conditions.items())
            for i in range(len(kv)):
                temp = ", " if i != len(kv) - 1 else " "
                sql = sql + str(kv[i][0]) + " = ?" + temp
                tempd.append(kv[i][1])
        data = tuple(tempd)

        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.update(sql=sql, conn=conn, data=data)
        db.close(conn)

        return r