#BIRTHDAY CHOCOLATE

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthday function below.
def birthday(s, d, m):
    
    # a =  [s[i:i+m] for i in range(len(s))]
    # return sum( sum(i)==d for i in a)
    return sum( sum(s[i:i+m])==d for i in range(len(s)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
