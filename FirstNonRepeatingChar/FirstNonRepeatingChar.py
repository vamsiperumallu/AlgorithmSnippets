#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    21-Dec-2021
Purpose: Given a string text1, return the First Non Repeating Character

Example1: 
 Input: text1 = "aaabcccdeeef"
 Output: b

Example2: 
 Input: text1 = "abcbad"
 Output: c

Example3: 
 Input: text1 = "abcabcabc"
 Output: ''
"""
def getFirstNonRepeatingChar(s):

      i = 0
      uniqueStr1 = ''
      for c in s:
            if(c not in s[:i-1] and c not in s[i+1:]):
                  uniqueStr1 += c
            i += 1
      if len(uniqueStr1)>0:
            return uniqueStr1[0]
      else:
            return None
                  
if __name__ == "__main__":
    
    print("#####################################################################")

    input = "aaabcccdeeef" 
    print("input:",input)
    print("First Non Repeating Character:", getFirstNonRepeatingChar(input))
    
    print("#####################################################################")
    input = "abcbad"
    print("input:",input)
    print("First Non Repeating Character:", getFirstNonRepeatingChar(input))

    print("#####################################################################")
    
    input = "abcabcabc"
    print("input:",input)
    print("First Non Repeating Character:", getFirstNonRepeatingChar(input))

    print("#####################################################################")  
###############################################################################
