#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    22-Dec-2021
Purpose: Given two sorted linked lists, merge them so that the resulting linked list is also sorted.        

Example1: 
 Input1 = [4,8,15,19]
 Input2 = [7,9,10,16]
 Output = [4,7,8,9,10,15,16,19]

 Input1 = [1,2,5,6]
 Input2 = [3,4,7,8]
 Output = [1,2,3,4,5,6,7,8]
###############################################################################
Time Complexity:  O(n)
Space Complexity: O(n) 
"""
class Node:
    def __init__(self,value = None):
        self.value = value
        self.nextNode  = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        if(self.head == None):
            self.head = Node(value)
        else:
            self.__insert(self.head,value)
    
    def __insert(self,curr,value):
        if(curr.nextNode == None):
            curr.nextNode = Node(value)
            return
        else:
             self.__insert(curr.nextNode,value)

    def printSLL(self):
        if(self.head != None):
            list1 = []
            self.__printSLL(self.head,list1)
            print(list1)
        else:
            print("No elements in the Single Linked List") 
    
    def __printSLL(self,curr,list1):
        list1.append(curr.value)
        if(curr.nextNode != None):
            self.__printSLL(curr.nextNode,list1)

def createSingleLinkedList(inpList):
    sll1 = SingleLinkedList()
    for value in inpList:
        sll1.insert(value)
    return sll1

def mergeSortedLinkedLists(head1, head2):

    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    output = SingleLinkedList()
      
    while (head1 != None and head2 != None):
        if(head1.value < head2.value):
            output.insert(head1.value)
            head1 = head1.nextNode
        else:
            output.insert(head2.value)
            head2 = head2.nextNode

    while (head1 != None):
        output.insert(head1.value)
        head1 = head1.nextNode
    while (head2 != None):
        output.insert(head2.value)
        head2 = head2.nextNode
    return output
                  
if __name__ == "__main__":
    
    print("#####################################################################")
    input1 = [4,8,15,19]
    sll1 = createSingleLinkedList(input1)
    input2 = [7,9,10,16]
    sll2 = createSingleLinkedList(input2)
    print("Input Sorted Linked List1:")
    sll1.printSLL()
    print("Input Sorted Linked List2:")
    sll2.printSLL()
    print("Merged Sorted Linked List:")
    mergeSortedLinkedLists(sll1.head, sll2.head).printSLL()
    print("#####################################################################")
    input1 = [1,2,5,6]
    sll1 = createSingleLinkedList(input1)    
    input2 = [3,4,7,8]
    sll2 = createSingleLinkedList(input2)
    print("Input Sorted Linked List1:")
    sll1.printSLL()
    print("Input Sorted Linked List2:")
    sll2.printSLL()
    print("Merged Sorted Linked List:")
    mergeSortedLinkedLists(sll1.head, sll2.head).printSLL()
    print("#####################################################################")    
###############################################################################
