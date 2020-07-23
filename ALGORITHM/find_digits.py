#FIND DIGITS

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    dividend = n
    count = sum( dividend%int(i)==0 for i in str(n) if(i!='0'))
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
