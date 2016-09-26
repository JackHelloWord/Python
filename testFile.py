#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开一个文件
fo = open("templeate/install.sls", "r")
for i in fo:
    i = i.replace("<#path#>", "O(∩_∩)O")
    print(i)
if not fo.closed:
    fo.close()
print(fo.closed)
