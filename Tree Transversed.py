# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 03:16:06 2019

@author: vinay
"""

'''
Tree Transversed Algorithm
'''
# IN-order Traversal
# left Subtree visited first , then root and then Right Subtree

#create node : 
class Node:
#constructor to build node 
    def __init__ (self, data) :
        self.left = None
        self.right = None
        self.data = data

#Add insertion method to insert data in Tree
    def insertion(self , data):
        if self.data:
            if data < self.data: #condition of comparision
                if self.left is None : 
                    self.left = Node(data) 
                else:
                    self.left.insertion(data)
            elif data > self.data : 
                if self.right is None: 
                    self.right = Node(data)
                else: 
                    self.right.insertion(data)
            else: 
                self.data = data
                 #method to print tree
    def PrintTree (self) :
        print (self.data),
        if self.right :
            self.right.PrintTree()
    
    #in-oder Traversal (left then root then right)
    def inorder(self, root):
        answer = []
        if root : 
            answer = self.inorder(root.left)
            answer.append(root.data)
            answer = answer + self.inorder(root.right)
        return answer
 
    #pre-oder Traversal ( root then  left  then right)
    def preorder(self, root):
        answer = []
        if root : 
            answer.append(root.data)
            answer = answer + self.preorder(root.left)
            answer = answer + self.preorder(root.right)
        return answer
    
    #post oder Traversal ( left then  right  then root)
    def postorder(self, root):
        answer = []
        if root : 
            answer = answer + self.preorder(root.left)
            answer = answer + self.preorder(root.right)
            answer.append(root.data)
        return answer
 
#driver Code : 
root = Node(30)
root.insertion(12)
root.insertion(14)
root.insertion(56)
root.insertion(23)
root.insertion(89)
root.insertion(52)
root.insertion(22)
print (' In-order :  ', root.inorder(root))
print (' Pre-Order : ' , root.preorder(root))
print (' Post - Order :',root.postorder(root))

