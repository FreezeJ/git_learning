#!/usr/bin/env python
# coding=utf-8
import random
num_list = []
for i in range(100):
    num_list.append(random.randint(1,1001))
max_num = 0
for i in num_list:
    if max_num < i:
        max_num = i
print "max number is", max_num
print num_list
