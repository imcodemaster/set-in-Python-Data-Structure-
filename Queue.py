# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 04:03:16 2019

@author: vinay
"""

'''
Queue

First In First Out
'''
class Queue :  #Creating class named Queue
    def __init__(self) : #constructor 
        self.queue = list()
        
    def add (self, data) : #Method to add a element in Queue (use insert method) 
        if data not in self.queue:
            self.queue.insert(0, data)
            return True
        return False 
    
    def size(self): # Method To get the size of Queue
        return len(self.queue)
    
    #Removing 
# Use POP method 
    def remove (self) :
        if len(self.queue ) > 0 :
            return self.queue.pop()
        return ('Last added element is Pop')

    
    def print (self):
        print (self.queue)
    
#Driver Code : 
MyQueue = Queue()
MyQueue.add('a')
MyQueue.add('b')
MyQueue.add('c')
MyQueue.add('d')
MyQueue.add('e')
MyQueue.add('f')
MyQueue.add('g')
MyQueue.add('h')
MyQueue.add('i')
MyQueue.add('j')

print ('size of Queue : ' , MyQueue.size())
print (MyQueue.print())
print ('removed : ' , MyQueue.remove())
print (MyQueue.print())

#Why This None Is Showing after printing A QUEUE ? 



