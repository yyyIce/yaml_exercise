#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import json

file_path = "./04_ref_yaml.yml"
file = open(file_path, 'r')
# 读取包含一个yml文档对象的yml文件
yml_content = yaml.load(file.read(), Loader=yaml.Loader)
print(yml_content)
print(json.dumps(yml_content, indent=2))
