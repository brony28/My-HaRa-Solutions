#VIRAL ADVERTISING


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    i = 5
    cumul=0
    for _ in range(n):
        likes = math.floor(i/2)
        cumul = cumul + likes
        i = likes*3

    return cumul

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
