#!/usr/bin/python
# -*- coding: UTF-8 -*-

' 测试salt '
__author__ = 'Jack Qin'

import salt.client as sc
import json

###salt调用
local = sc.LocalClient()

###目标主机指定
tgt = "minion134"

result = local.cmd("*", "test.ping")