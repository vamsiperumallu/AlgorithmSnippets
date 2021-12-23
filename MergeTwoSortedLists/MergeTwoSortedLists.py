#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    22-Dec-2021
Purpose: Given two sorted lists, merge them so that the resulting list is also sorted.        

Example1: 
 Input1 = [4,8,15,19]
 Input2 = [7,9,10,16]
 Output = [4,7,8,9,10,15,16,19]

 Input1 = [1,2,5,6]
 Input2 = [3,4,7,8]
 Output = [1,2,3,4,5,6,7,8]
###############################################################################
Time Complexity:  O(n+m)
"""
def mergeSortedLists(input1, input2):

      n = len(input1)
      m = len(input2)

      output = []
      
      i = j = 0
      while (i < n and j < m):
          if(input1[i] < input2[j]):
              output.append(input1[i])
              i += 1
          else:
              output.append(input2[j])
              j += 1
      while (i < n):
          output.append(input1[i])
          i += 1
      while (j < m):
          output.append(input2[j])
          j += 1
      return output
                  
if __name__ == "__main__":
    
    print("#####################################################################")
    input1 = [4,8,15,19]
    input2 = [7,9,10,16]
    print("Input Sorted List1:",input1)
    print("Input Sorted List2:",input2)    
    print("Merged Sorted List:", mergeSortedLists(input1, input2))
    print("#####################################################################")
    input1 = [1,2,5,6]
    input2 = [3,4,7,8]
    print("Input Sorted List1:",input1)
    print("Input Sorted List2:",input2)    
    print("Merged Sorted List:", mergeSortedLists(input1, input2))
    print("#####################################################################")    
###############################################################################
