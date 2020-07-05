#SOCK MERCHANT


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter,OrderedDict

# Complete the sockMerchant function below.
class OrderedCounter(Counter,OrderedDict):
    pass

def sockMerchant(n, ar):
    a = OrderedCounter(ar)
    return sum(i//2 for i in a.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
