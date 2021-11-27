#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    26-Nov-2021
Purpose: This script will generate Finocci series using 3 approaches
         1) Using normal For loop
         2) Using Recursive function call
         3) Using Dynamic Programming – Memoization
"""
###############################################################################
#For loop - Time Complexity: O(n)
###############################################################################
def getFibnocciSize_1(n):
    
    if n <= 0:
        return 0
    a = 0
    b = 1
    c = 0
            
    for i in range(1,n):
        c = a + b
        a = b
        b = c
    return c

def generateFibnocci_1(n):
    
    if n <= 0:
        return 0
    
    a = 0
    b = 1
    c = 0
    series = [0]
            
    for i in range(1,n+1):
        if i < 2:
            series.append(1)
        else:
            c = a + b
            series.append(c)
            a = b
            b = c
    return series

###############################################################################
#Recursive function - Time Complexity:
#T(n) = T(n-1) + T(n-2) + 1 = 2n = O(2^n)
###############################################################################
def getFibnocciSize_2(n):
    
    if n <= 0:
        return  0
    
    if n < 2:
        return 1
    else:
        return getFibnocciSize_2(n-1)+getFibnocciSize_2(n-2)

def generateFibnocci_2(n,series=[0,1]):
    
    if (n <= 0):
        return 0 

    if n < 2:
        yield series
    else:
        yield from generateFibnocci_2(n-1,series+[series[-1]+series[-2]])
        
###############################################################################
#Dynamic Programming – Memoization - Time Complexity: O(n)
###############################################################################
def getFibnocciSize_3(n):
    
    if n <= 0:
        return  0
    
    series = [0,1]
    
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
    return series[-1]

def generateFibnocci_3(n):
    
    if n <= 0:
        return  0
    
    series = [0,1]
    
    for i in range(2,n+1):
        series.append(series[i-1] + series[i-2])
    return series
###############################################################################
if __name__ == "__main__":
    
    for i in range(-1,8):
        print(getFibnocciSize_1(i))
        print(generateFibnocci_1(i))

        print(getFibnocciSize_2(i))
        print(list(generateFibnocci_2(i)))

        print(getFibnocciSize_3(i))
        print(generateFibnocci_3(i))
        print("-------------------------------------")