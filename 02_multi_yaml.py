#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml

file_path = "./02_multi_yaml.yml"
file = open(file_path, 'r')
# 解析包含多个YAML文件的yml文件
yml_content = yaml.load_all(file.read(), Loader=yaml.Loader)
for yml_i in yml_content:
   print(yml_i)
   print(type(yml_i))
