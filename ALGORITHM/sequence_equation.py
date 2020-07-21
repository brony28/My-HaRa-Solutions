#SEQUENCE EQUATION


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    y=[]
    for i in range(1,n+1):
        indexOfi = p.index(i)+1
        y.append(p.index(indexOfi)+1)
    return y

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

















# Nicely explained here (also check its comments): 
# https://www.hackerrank.com/challenges/permutation-equation/forum/comments/278763