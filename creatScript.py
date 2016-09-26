#!/usr/bin/python
# -*- coding: UTF-8 -*-

' 创建安装脚本 '
__author__ = 'Jack Qin'

import os
import sys
sys.path.append("conf")
import config

class CreateScript:
    def __init__(self):
        self.configs = config.configs
        self.templeateDir = 'templeate'

    def creatFile(self, sFile, tFile):
        print(sFile)
        print(tFile)
        fo = open(sFile, "r", 1024)
        fw = open(tFile, "w", 1024)

        for i in fo:
            for type in self.configs:
                for key in self.configs[type]:
                    i = i.replace("<#"+key+"#>", self.configs[type][key])
            fw.write(i)
        fo.flush()
        fw.flush()
        if not fo.closed:
            fo.close()
        if not fw.closed:
            fo.close()

    def creatFiles(self):
        for parent, dirnames, files in os.walk(self.templeateDir):
            for filename in files:
                self.creatFile(parent+os.sep+filename,os.path.abspath(self.configs['salt']['salt_path'])+os.sep+filename)

test = CreateScript()
test.creatFiles()
