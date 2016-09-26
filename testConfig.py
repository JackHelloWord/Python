#!/usr/bin/python
# -*- coding: UTF-8 -*-
' test config '
__author__ = 'Jack Qin'

import sys
sys.path.append("conf")
import config

configs = config.configs

print(configs['db']['db_port'])