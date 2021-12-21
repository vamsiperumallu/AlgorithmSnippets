#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    27-Nov-2021
Purpose: This script will get the Longest Substring using 2 approaches
         1) Using Recursive function call
         2) Using Dynamic Programming

Problem: Given a string text1, return the length of their longest substring.

Example1: 
 Input: text1 = "abcabcbb"
 Output: 3  (abc)

Example2: 
 Input: text1 = "bbbbb"
 Output: 1  (b)

Example3: 
 Input: text1 = "pwwkew"
 Output: 3  (wke)
"""
def lengthOfLongestSubstring(s):
      maxlen = 0
      str1 = "" 

      for c in s:
            if(c in str1):
                  maxlen = max(maxlen,len(str1))
                  str1 = str1[str1.find(c)+1:] + c
            else:
                  str1 += c
      return max(maxlen,len(str1))      
                  
if __name__ == "__main__":
    
    print("#####################################################################")

    input = "abcabcbb" 
    print("input:",input)
    print("Longest Substring:", lengthOfLongestSubstring(input))
    
    print("#####################################################################")
    input = "bbbbb"
    print("input:",input)
    print("Longest Substring:", lengthOfLongestSubstring(input))

    print("#####################################################################")
    
    input = "pwwkew"
    print("input:",input)
    print("Longest Substring:", lengthOfLongestSubstring(input))

    print("#####################################################################")

    input = "qwertyabcdaef"
    print("input:",input)
    print("Longest Substring:", lengthOfLongestSubstring(input))

    print("#####################################################################")  
###############################################################################
