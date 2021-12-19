#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
###################################################################################
Author:  Vamsi Yalamanchili
Date:    18-Dec-2021

Problem: Given an array containing sequence of bits (0 or 1), you have to sort this array in the such a way that all 0's should be on one side (either left or right)
         and all 1's on the other side. The constraints is that you can swap only the adjacent elements in the array. Find the minimum number of swaps required to 
         sort the given input array. This fucntion should return the minimum number of swaps required to sort these 0's and 1's.

Example1: 
 Input: [0,0,1,0,1,0,1,1]
 Output: 3

Example2: 
 Input: [1,1,1,1,0,0,0,0]
 Output: 0
###################################################################################
 Time Complexity:

  O(n) - As we need to loop through all the values in input List
###################################################################################
"""
def minSwaps(inpList):

    num_of_zeros = num_of_ones = cnt_of_zeros = cnt_of_ones = 0

    len1 = len(inpList)

    for p in range(0,len1):
        if(inpList[p] == 0):
           num_of_zeros += p - cnt_of_zeros
           cnt_of_zeros += 1 
        else:
           num_of_ones += p - cnt_of_ones
           cnt_of_ones += 1            
    return min(num_of_zeros, num_of_ones)

if __name__ == "__main__":

    inpList = [0,0,1,0,1,0,1,1]
    print("#####################################################################################")    
    print("Input List:", inpList)
    print("Minimum Swaps:", minSwaps(inpList))
    print("#####################################################################################")
    inpList = [1,1,1,1,0,0,0,0]

    print("Input List:", inpList)
    print("Minimum Swaps:", minSwaps(inpList))
    print("#####################################################################################")    