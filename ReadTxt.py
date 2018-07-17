# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 08:50:57 2018

@author: 长风振林
"""

import os

f=open("E:/皓首穷经/大四下/竞赛/京东/车辆智能调度-A榜/input_distance-time.txt","r")
lines=f.readlines()
data=[]
for line in lines:
    line=line.strip("\n")
    line=line.split(",")
    data.append(line)
    
    
print(data[10])