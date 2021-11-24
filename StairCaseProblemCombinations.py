# -*- coding: utf-8 -*-
"""
Author:  Vamsi Yalamanchili
Date:    23-Nov-2021
Purpose: Script for counting Stair Case

Problem:
Say, you are climbing a stair case. It takes n steps to reach to the top. 
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Display the total steps needed and combinations
Note: Given n will be a positive integer.
"""
# n - Total no of steps to be climbed
# 2 steps can be climbed each time
def stairCaseCount(n):
    if n<=1: return 1
    return stairCaseCount(n-1)+stairCaseCount(n-2)

def generateCombinations(n, x, current=[0]):
  if current[-1] == n:
      yield current
  else:
    for i in x:
      if current[-1]+i <= n:
          yield from generateCombinations(n,x,current+[current[-1]+i])

if __name__ == "__main__":
    
    n = 5
    x = [1,2]
    steps = stairCaseCount(n)
    resultList = list(generateCombinations(n,x))
    
    print("No of combinations that we can climb",n,"Steps are:", steps)
    print("Combinations: ", resultList)