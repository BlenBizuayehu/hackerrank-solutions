#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[n - 1]          # Store the last element
    i = n - 2                   # Start comparing from second last index
    
    # Move elements greater than value one position ahead
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    
    # Insert the stored value at correct position
    arr[i + 1] = value
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)