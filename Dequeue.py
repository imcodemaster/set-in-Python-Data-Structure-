# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 04:23:00 2019

@author: vinay
"""

'''
Dequeue
'''
import collections

dbend = collections.deque(['vinay', 'vivek', 'vaishali']) 
print (dbend)
dbend.append('Bhoomi')  
#apend add the right position
print ('Append at right : ' , dbend)
#Append at left side  (append on both end)
dbend.appendleft ('Himanshi')
print ('Append at Left : ' , dbend)

#removing from right 
dbend.pop()
print ('Pop at right : ' , dbend)
#remoing from left 
dbend.popleft()
print ('Pop at right : ' , dbend)
