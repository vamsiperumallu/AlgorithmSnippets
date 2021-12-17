#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    17-Dec-2021
Purpose: This script will generate the encoding for Run Length

Example: 
    Input : aaaabbcc
    Output: 4a2b2c

    Input : aaaabbccaa
    Output: 4a2b2c2a
"""

def generateEncoding(inpStr):
    encodedStr = ""
    prevChar = ''
    curLen = 0
    firstTime = True
    for currChar in inpStr:
     #   print(prevChar, currChar, curLen)
        if firstTime:
            prevChar = currChar
            curLen += 1
            firstTime = False
        elif prevChar == currChar:
            curLen += 1
        else:
            encodedStr = encodedStr + str(curLen) + prevChar
            curLen = 1
            prevChar = currChar
    encodedStr = encodedStr + str(curLen) + prevChar            
    return encodedStr    

if __name__ == "__main__":

    input1 = "aaaabbcc"
    print("Input String: ",input1)

    print("Encoded String: ", generateEncoding(input1))

    input1 = "aaaabbccaa"
    print("Input String: ",input1)

    print("Encoded String: ", generateEncoding(input1))    
