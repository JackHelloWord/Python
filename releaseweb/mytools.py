#!/usr/bin/python
# -*- coding: UTF-8 -*-

' mytools '
__author__ = 'Jack Qin'
from os.path import basename, isdir
from os import listdir
import os
import shutil
import re

source = "D:/SRM云测试环境/SRMGit/goinglinkcloud"

def writeTree(path, depth=0):
    print(depth * '| ' + '|_', basename(path))
    if (isdir(path)):
        for item in listdir(path):
            traverse(path + '/' + item, depth + 1)

def getFileList(dir, depth=0):
    for dirpath, dirnames, filenames in os.walk(dir):
        print('Directory', dirpath)
        for filename in filenames:
            print(' File', filename)

def fetchFile(filelistname, tgdirectory, printlog=False):
    #判断目标文件夹是否存在，如果存在，则删除
    if os.path.isdir(tgdirectory):
        try:
            shutil.rmtree(tgdirectory)
        except Exception:
            print(tgdirectory + " is exist! remove it error")
            exit(1)
        else:
            print(tgdirectory + " is exist! remove it success")

    filelist = open(filelistname)
    for line in filelist:
        #去空行
        if not line.split():
            continue;
        line = formatstr(line)
        #判断是否以modules开头
        if line.startswith("modules"):
            line = "webRoot/" + line
        #判断是否以classes开头
        if line.startswith("classes"):
            line = "webRoot/WEB-INF/" + line

        #拼接原路径与目标路径
        sr = formatstr(source) + "/" + line
        tg = formatstr(tgdirectory) + "/" +line

        flag = copy(sr, tg)
        if flag == 0:
            if printlog:
                print(tg)
        elif flag == -1:
            print("File " + sr + " is not exist")
        else:
            print("copy file " + sr + " has some Exception")
            print(flag)

def copy(sfile, tfile):
    if not os.path.exists(sfile):
        return -1
    p, src_name = os.path.split(tfile)
    print("p: " + p)
    print("s: " + src_name)
    try:
        if not os.path.isdir(p):
            os.makedirs(p)
        if os.path.isfile(sfile):
            shutil.copyfile(sfile, tfile)
        else:
            shutil.copytree(sfile, tfile)
    except Exception as e:
        return e
    else:
        return 0

def formatstr(str):
    # 去空白字符串
    str = re.sub('(\s)*', '', str)
    # 替换"\\"或"//"为/
    str = re.sub('((\\\\)+)|/(/+)', '/', str)
    # 去开头和结尾的/
    if str.startswith("/"):
        str = str[1:]
    if str.endswith("/"):
        str = str[:len(str) - 1]

    return str

if __name__ == '__main__':
    fetchFile("filelist", "copyfile", True)