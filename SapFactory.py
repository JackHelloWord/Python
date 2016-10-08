#!/usr/bin/python
# -*- coding: UTF-8 -*-

' SAP '
__author__ = 'Jack Qin'

import sys
sys.path.append("conf")
import config
import DbFactory
import os
import traceback

class SapFactory:
    def __init__(self):
        pass

    def save_sap_conf(self):
        sap_config = config.configs["sap"]
        mule_config = config.configs["mule"]

        sap_name = mule_config["mule_name"]
        jco_sysnr = sap_config["jco_sysnr"]
        gateway_host = sap_config["gateway_host"]
        sap_router = sap_config["sap_router"]
        jco_client = sap_config["jco_client"]
        jco_user = sap_config["jco_user"]
        jco_passwd = sap_config["jco_passwd"]
        jco_lang = sap_config["jco_lang"]
        respository_destination = sap_config["respository_destination"]
        repository_name = sap_config["repository_name"]

        return self.save_sap(sap_name,
                             jco_sysnr,
                             gateway_host,
                             sap_router,
                             jco_client,
                             jco_user,
                             jco_passwd,
                             jco_lang,
                             respository_destination,
                             repository_name)


    def save_sap(self,
                 sap_name,
                 jco_sysnr,
                 gateway_host,
                 sap_router,
                 jco_client,
                 jco_user,
                 jco_passwd,
                 jco_lang,
                 respository_destination,
                 repository_name):
        sap_data = [(sap_name,
                     jco_sysnr,
                     gateway_host,
                     sap_router,
                     jco_client,
                     jco_user,
                     jco_passwd,
                     jco_lang,
                     respository_destination,
                     repository_name),
                    ]
        sql = "install INTO mule (" \
              "sap_name,jco_sysnr," \
              "gateway_host,sap_router" \
              ",jco_client," \
              "jco_user,jco_passwd," \
              "jco_lang," \
              "respository_destination," \
              "repository_name" \
              ") " \
              "VALUES(?,?,?,?,?,?,?,?,?,?)"

        db = DbFactory(True)
        conn = db.get_conn(db.get_sqlite_path())
        r = db.save(sql=sql,conn=conn, data=sap_data)
        db.close(conn)

        return r

    def fetchall(self):
        sql = "select * from sap"
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

        sql = sql + "from sap "

        if len(conditions) != 0:
            if not isinstance(paramaters, tuple):
                conditions = (conditions,)
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