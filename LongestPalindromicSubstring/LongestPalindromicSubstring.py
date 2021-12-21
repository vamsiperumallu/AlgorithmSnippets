#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    21-Dec-2021
Purpose: Given a string text1, return the longest palindromic substring in s.

Example1: 
 Input: text1 = "babad"
 Output: "bab"

Example2: 
 Input: text1 = "cbbd"
 Output: "bb"

Example3: 
 Input: text1 = "abcba"
 Output: "abcba"

Example4: 
 Input: text1 = "abcdba"
 Output: "a"
"""
def isPalindrome(s):
      left = 0
      right = len(s)-1
      ret = True
      while(left < right):
            if(s[left]!= s[right]):
                  ret = False
                  break
            else:
                  left  += 1
                  right -= 1
      #print(s,left,right,ret)                  
      return ret

def longestPalindrome(s):
      maxlen = 0
      retStr = "" 
      len1 = len(s)
      for i in range(0,len1):
            for j in reversed(range(i,len1+1)):
                  if(isPalindrome(s[i:j])):
                        if(len(s[i:j]) > maxlen):
                              retStr = s[i:j]
                              maxlen = len(s[i:j])
      if(len(s[i:j]) > maxlen):
            retStr = s[i:j]
      return retStr
                  
if __name__ == "__main__":
    
    print(isPalindrome("malayalam"))
    print("#####################################################################")
    input = "babad" 
    print("input:",input)
    print("Longest Palindromic Substring:", longestPalindrome(input))
    
    print("#####################################################################")
    input = "cbbd"
    print("input:",input)
    print("Longest Palindromic Substring:", longestPalindrome(input))

    print("#####################################################################")
    
    input = "abcba"
    print("input:",input)
    print("Longest Palindromic Substring:", longestPalindrome(input))

    print("#####################################################################")

    input = "abcdba"
    print("input:",input)
    print("Longest Palindromic Substring:", longestPalindrome(input))

    print("#####################################################################")
###############################################################################
