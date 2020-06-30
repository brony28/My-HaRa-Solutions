#BREAKING THE RECORDS



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    hc = 0
    lc = 0
    high = scores[0]
    low = scores[0]
    for i in scores[1:]:
        if(i>high):
            hc+=1
            high = i
        elif(i<low):
            lc+=1
            low = i
    return [hc,lc]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()








'''
def breaking_records(score):

hs = [ i for i,item in enumerate(scores[1:]) if item>max(scores[0:i+1]) ]

ls = [ i for i,item in enumerate(scores[1:]) if item

return [len(hs), len(ls)]
'''