#MIGRATORY BIRDS


#refered from Discussions... Complexity check(Y)

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

# Complete the migratoryBirds function below.


# class OrderedCounter(Counter,OrderedDict):
#     pass

def migratoryBirds(arr):
    # a = OrderedCounter(arr)
    # return a.most_common(1)[0][0]
    count = [0]*6
    for i in arr:
        count[i]+=1
    return count.index(max(count))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()



# link : https://www.hackerrank.com/challenges/migratory-birds/forum