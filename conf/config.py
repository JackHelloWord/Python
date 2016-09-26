#!/usr/bin/python
# -*- coding: UTF-8 -*-

' default config '

__author__ = 'Jack Qin'

configs = {
    'salt': {
        'salt_path': 'E:\\test'
    },
    'mule': {
        'mule_home': '/home/muleManager',
        'mule_name': 'danz',
        'config_name': 'server1.properties.standalone',
        'config_resources': 'idocUncompress.xml,idocSync.xml,idocParser.xml,global.xml,sapReceive.xml'
    },
    'db': {
        'db_host': '172.20.0.199',
        'db_port': '1521',
        'db_user': 'cloudtrain',
        'db_password': 'handcloudtrain',
        'db_name': 'CLOUDTRAIN'
    },
    'sap': {
        'program_id': 'scfidoc',
        'repository_name': 'ED1',
        'jcoSysnr': '10',
        'gateway_host': '10.52.15.155',
        'SAProuter': '/H/113.105.5.250/H/',
        'jcoClient': '200',
        'jcoUser': 'HANDSRM',
        'jcoPasswd': 'handhand',
        'jcoLang': 'ZH',
        'respository_destination': 'BCE'
    }
}