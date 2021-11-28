#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    27-Nov-2021
Purpose: This script will get the Longest Subsequence using 2 approaches
         1) Using Recursive function call
         2) Using Dynamic Programming

Problem: Given two strings text1 and text2, return the length of their longest 
         common subsequence. If there is no common subsequence, return 0.

Example1: 
 Input: text1 = "abcde", text2 = "ace" 
 Output: 3  

Example2: 
 Input: text1 = "abc", text2 = "abc"
 Output: 3

Example3: 
 Input: text1 = "abc", text2 = "def"
 Output: 0

Example4: 
 Input: text1 = "abcde", text2 = "fde"
 Output: 2
"""
def getLongestSubsequence_1(n,m,input1,input2):
    
    if (n==0 or m==0): return 0
    
    elif (input1[n-1]==input2[m-1]):
        return 1+getLongestSubsequence_1(n-1,m-1,input1,input2)
    
    else:
        return max(getLongestSubsequence_1(n-1,m,input1,input2),\
                   getLongestSubsequence_1(n,m-1,input1,input2))

def getLongestSubsequence_2(n,m,input1,input2,series=[]):
    
    if (n==0 or m==0): return 0
    
    elif (input1[n-1]==input2[m-1]):
        return 1+getLongestSubsequence_2(n-1,m-1,input1,input2,\
                                         series+[input1[n-1]])
    
    else:
        return max(getLongestSubsequence_2(n-1,m,input1,input2,\
                                           series+[input1[n-1]]),\
            getLongestSubsequence_2(n,m-1,input1,input2),\
            series+[input1[n-1]])
        
if __name__ == "__main__":
    
    input1 = ["a","b","c","d","e"]
    input2 = ["a","c","e"]
    
    n = len(input1)
    m = len(input2)
    
    print("Input1:",input1)
    print("Input2:",input2)    
    print("Longest Subsequence:",\
          getLongestSubsequence_1(n,m,input1,input2))
    
    print("Longest Subsequence:",\
          list(getLongestSubsequence_2(n,m,input1,input2)))  
    
    print("---------------------------------------------")

    input1 = ["a","b","c"]
    input2 = ["a","b","c"]
    
    n = len(input1)
    m = len(input2)
    
    print("Input1:",input1)
    print("Input2:",input2)    
    print("Longest Subsequence:",\
          getLongestSubsequence_1(n,m,input1,input2))
    
    print("Longest Subsequence:",\
          list(getLongestSubsequence_2(n,m,input1,input2))) 
    
    print("---------------------------------------------")

    input1 = ["a","b","c"]
    input2 = ["d","e","f"]
    
    n = len(input1)
    m = len(input2)
    
    print("Input1:",input1)
    print("Input2:",input2)    
    print("Longest Subsequence:",\
          getLongestSubsequence_1(n,m,input1,input2))
    
    print("Longest Subsequence:",\
          list(getLongestSubsequence_2(n,m,input1,input2)))  

    print("---------------------------------------------")

    input1 = ["a","b","c","d","e"]
    input2 = ["f","d","e"]
    
    n = len(input1)
    m = len(input2)
    
    print("Input1:",input1)
    print("Input2:",input2)    
    print("Longest Subsequence:",\
          getLongestSubsequence_1(n,m,input1,input2))
    
    print("Longest Subsequence:",\
          list(getLongestSubsequence_2(n,m,input1,input2)))

    print("---------------------------------------------")    
###############################################################################
