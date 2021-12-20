#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###################################################################################
Author:  Vamsi Yalamanchili
Date:    20-Dec-2021

Problem: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
         and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
         You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example1: 
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example2: 
Input: l1 = [0], l2 = [0]
Output: [0]

Example3: 
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
###################################################################################
 Time Complexity:

  O(n) - As we need to loop through all the values in input List
###################################################################################
"""
def getReverseIntOfList(lst):
    len1 = len(lst)
    num = ''
    for i in lst:
        num = str(i)+num
    print(num)    
    return int(num)

def getReverseListOfInt(out):
    outList = []
    for i in reversed(str(out)):
        outList.append(i)
    return outList

def addTwoNumbers(l1,l2):
    return getReverseListOfInt(getReverseIntOfList(l1) + getReverseIntOfList(l2))

if __name__ == "__main__":

    print("#####################################################################################")  
    l1 = [2,4,3]
    l2 = [5,6,4]  
    print("Input List1:", l1)
    print("Input List2:", l2)    
    print("Output List:", addTwoNumbers(l1,l2))
    print("#####################################################################################")
    l1 = [0]
    l2 = [0]  
    print("Input List1:", l1)
    print("Input List2:", l2)    
    print("Output List:", addTwoNumbers(l1,l2))
    print("#####################################################################################")
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    print("Input List1:", l1)
    print("Input List2:", l2)    
    print("Output List:", addTwoNumbers(l1,l2))
    print("#####################################################################################")     

    print(7%10)