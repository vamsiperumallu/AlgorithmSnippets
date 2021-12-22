#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    22-Dec-2021
Purpose: Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.
         Return true if the sum exists and return false if it does not.

Example1: 
 Input: [5,7,1,2,8,4,3] and 10
 Output: True

Example2: 
 Input: [1,2,3,4,5,6] and 7
 Output: True

Example3: 
 Input: [5,7,1,2,8,4,3] and 19
 Output: False
###############################################################################
Time Complexity:  O(n)
Space Complexity: O(n) 
"""
def findSumOfTwoIntegers(inp1, value):

      n = len(inp1)
      inp1.sort()
      for i in range(0,n):
          if(value-inp1[i] in inp1[i+1:]):
              return True
      return False
                  
if __name__ == "__main__":
    
    print("#####################################################################")

    input = [5,7,1,2,8,4,3]
    value = 10
    print("input:",input)
    print("Missing Number in Array:", findSumOfTwoIntegers(input, value))
    
    print("#####################################################################")
    input = [1,2,3,4,5,6]
    value = 7
    print("input:",input)
    print("Missing Number in Array:", findSumOfTwoIntegers(input, value))

    print("#####################################################################")
    
    input = [5, 7, 1, 2, 8, 4, 3]
    value = 2
    print("input:",input)
    print("Missing Number in Array:", findSumOfTwoIntegers(input, value))

    print("#####################################################################")  
###############################################################################
