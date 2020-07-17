#BEAUTIFUL DAYS AT THE MOVIES


	#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count = 0
    for days in range(i,j+1):
        rev_days = str(days)[::-1]
        if(abs(days-int(rev_days))%k==0):
            count=count+1
    return count

    #2 line code
    # count = sum( abs(days-int(str(days)[::-1]))%k==0 for days in range(i,j+1))
    # return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
