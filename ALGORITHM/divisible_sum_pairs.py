#DIVISIBLE SUM PAIRS


#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations


# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    a = list(combinations(ar,2))
    return sum((i[0]+i[1])%k==0 for i in a)
    # return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


# https://www.hackerrank.com/challenges/divisible-sum-pairs/forum