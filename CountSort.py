"""Hacker Rank Challenege 
https://www.hackerrank.com/challenges/countingsort4/problem?isFullScreen=true

Use the counting sort to order a list of strings associated with integers. If two strings are associated with the same integer, they must be printed in their original order, i.e. your sorting algorithm should be stable. There is one other twist: strings in the first half of the array are to be replaced with the character - (dash, ascii 45 decimal).

Insertion Sort and the simple version of Quicksort are stable, but the faster in-place version of Quicksort is not since it scrambles around elements while sorting.

Design your counting sort to be stable.

Function Description

Complete the countSort function in python3. It should construct and print the sorted strings.

countSort has the following parameter(s):
string arr[n][2]: each arr[i] is comprised of two strings, x and s

Returns
- Print the finished array with each element separated by a single space.

Note: The first element of each arr[i],x, must be cast as an integer to perform the sort.

Input Format

The first line contains n, the number of integer/string pairs in the array arr.
Each of the next n contains x[i] and s[i], the integers (as strings) with their associated strings.
"""
#!/bin/python3

def countSort(arr):
    final_list = [[] for _ in range(len(arr))]

    for count, value in enumerate(arr):
        final_list[int(value[0])].append('-' if count < len(arr)//2 else value[1])

    print(' '.join(j for k in final_list for j in k))
    
n = int(input().strip())
arr = [input().rstrip().split() for _ in range(n)]
countSort(arr)


# Following code too works with higer Gas price
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    final_list = [[] for k in range(len(arr))]

    for count,value in enumerate(arr):
        if count < len(arr)//2:
            final_list[int(value[0])].append('-')
        else:
            final_list[int(value[0])].append(value[1])
    
    print(' '.join([j for k in final_list for j in k]))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
