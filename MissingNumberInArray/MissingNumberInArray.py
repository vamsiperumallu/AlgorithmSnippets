#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    22-Dec-2021
Purpose: Given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x. 
         You have to find x. The input array is not sorted.

Example1: 
 Input: [3,7,1,2,8,4,5]
 Output: 6

Example2: 
 Input: [1,8,6,5,4,3,7,9]
 Output: 2

Example3: 
 Input: [1,8,6,5,4,3,7,2]
 Output: 9
###############################################################################
Time Complexity:  O(n)
Space Complexity: O(1) 
"""
def findMissingNumber(inp1):

      n = len(inp1)+1                           #add 1 as we have 1 missing number

      list_sum = sum(inp1)
      expected_sum = int((n * (n+1)) / 2)       # To get the number sum in a series
      return (expected_sum - list_sum)
                  
if __name__ == "__main__":
    
    print("#####################################################################")

    input = [3,7,1,2,8,4,5]
    print("input:",input)
    print("Missing Number in Array:", findMissingNumber(input))
    
    print("#####################################################################")
    input = [1,8,6,5,4,3,7,9]
    print("input:",input)
    print("Missing Number in Array:", findMissingNumber(input))

    print("#####################################################################")
    
    input = [1,8,6,5,4,3,7,2]
    print("input:",input)
    print("Missing Number in Array:", findMissingNumber(input))

    print("#####################################################################")  
###############################################################################
