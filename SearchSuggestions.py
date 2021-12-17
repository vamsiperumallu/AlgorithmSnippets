#!/bin/python3

import math
import os
import random
import re
import sys


"""
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
There are no repeated elements in products.
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters.
"""

def lowerBound(repository, start, prefix):
    i = start
    j = len(repository)
    mid = 0
    
    while(i<j):
        mid = (i+j)//2
        if(repository[mid].lower()>=prefix.lower()):
            j = mid
        else:
            i = mid + 1         
    return i

def searchSuggestions(repository, customerQuery):
    # Write your code here
    repository = list(map(lambda d: d.lower(),repository))
    repository.sort()
    print(repository)
    print(customerQuery)        
    returnResult  = []
    
    start = bsStart = 0
    n = len(repository)
    
    prefix  = ''

    k = 0
    for c in customerQuery:
        prefix += c
        
        k += 1
        if(k<2):
            continue
        
        start = lowerBound(repository, bsStart, prefix)
        
        print(prefix,start, returnResult)
        
        localList = []
        for i in range(start,min(start+3,n)):
            
            print(len(repository[i]), len(prefix))
            print(repository[i][0:len(prefix)].lower(), prefix.lower())
            if(len(repository[i]) < len(prefix) or 
               (not repository[i][0:len(prefix)].lower()==prefix.lower())):
               break
            
            localList.append(repository[i])

        returnResult.append(localList)        
        bsStart = abs(start)
        
    return returnResult
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    repository_count = int(input().strip())

    repository = []

    for _ in range(repository_count):
        repository_item = input()
        repository.append(repository_item)

    customerQuery = input()

    result = searchSuggestions(repository, customerQuery)

    fptr.write('\n'.join([' '.join(x) for x in result]))
    fptr.write('\n')

    fptr.close()