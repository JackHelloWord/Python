#!/usr/bin/python
# -*- coding: UTF-8 -*-

' default config '

__author__ = 'Jack Qin'

configs = {
    'sqlite': {
        'sqlite_path': 'data/date.db'
    },
    'salt': {
        'salt_path': 'E:\\test'
    },
    'mule': {
        'mule_home': '/home/muleManager',
        'mule_name': 'danz',
		'program_id': 'scfidoc',
        'config_name': 'server1.properties.standalone',
        'config_resources': 'idocUncompress.xml,idocSync.xml,idocParser.xml,global.xml,sapReceive.xml'
    },
    'db': {
        'db_tns': '(DESCRIPTION='
                  '(ADDRESS_LIST='
                  '(LOAD_BALANCE=YES)'
                  '(FAILOVER=YES)'
                  '(ADDRESS=(PROTOCOL=tcp)(HOST=172.20.0.199)(PORT=1521)))'
                  '(CONNECT_DATA=(SERVICE_NAME=CLOUDTRAIN))'
                  ')',
        'db_user': 'cloudtrain',
        'db_password': 'handcloudtrain'
    },
    'sap': {
        'jco_sysnr': '10',
		'repository_name': 'ED1',
        'gateway_host': '10.52.15.155',
        'sap_router': '/H/113.105.5.250/H/',
        'jco_client': '200',
        'jco_user': 'HANDSRM',
        'jco_passwd': 'handhand',
        'jco_lang': 'ZH',
        'respository_destination': 'BCE'
    }
}