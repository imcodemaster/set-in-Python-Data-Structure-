# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 03:42:28 2019

@author: vinay
"""

'''
Creating a set : collection of item but not in any order 
'''
a = {'vinay', 'vikas', 'vishal' , 'vivek', 'vaishnavi'}
b = {12,2,4,5,6,7,87,5,3}

print ( 'set of names :' ,a)
print ('set of Number : ', b)

#Acessing Value : 
for i in a : 
   print ( 'iterate every element in set : ', i)
   
#Adding Value : 
a.add('Himanshi')
print (a)

#Removing Value :
a.discard('vishal')
print (a) 

#Union of Set 
d = {'himanshi, vaishali, neerajaa, Noori'}
c = a|b #Union of name and number 
f = a|d
print (c)
print (f)

#Difference of set
difference = a - d
print (difference)