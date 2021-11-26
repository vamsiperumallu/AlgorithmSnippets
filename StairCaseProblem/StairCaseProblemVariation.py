# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    23-Nov-2021
Purpose: Script for counting Stair Case

Problem:
Say, you are climbing a stair case. It takes n steps to reach to the top. 
Each time you can either climb x[1,3,5..] steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.
"""
# n - Total no of steps to be climbed
# 2 steps can be climbed each time
def stairCaseCount(n):
    if n<=1:
        return 1
    return stairCaseCount(n-1)+stairCaseCount(n-2)

def stairCaseVariationCount(n,x):
    if n == 0: return 1
    total = 0
    for i in x:
        if n-i >= 0:
            print("befor:",n,i,total)
            total = total + stairCaseVariationCount(n-i,x)
            print("after:",n,i,total)            
    return total

if __name__ == "__main__":
    
    n = 5
    x = [1,3,5]
    steps = stairCaseVariationCount(n,x)
    
    print("No of combinations that we can climb ",n,"Steps are:", steps)
    