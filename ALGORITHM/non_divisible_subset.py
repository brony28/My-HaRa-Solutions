#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    if(k==0 or k==1):
        return 1
    d={}
    for i in s:
        if(i%k in d):
            d[i%k]+=1
        else:
            d[i%k]=1
    print(d)
    remainders=list(d.keys())
    newList=[]

    # if(k - remainders[0]==remainders[0]):
    #     newList = newList + [remainders[0]]
    #     remainders.remove(remainders[0])
    while(len(remainders)!=0):
        # if(remainders[0]==0):    
        #     newList = newList + [remainders[0]]
        #     remainders.remove(remainders[0])
        if (k - remainders[0]) in remainders and abs(2*remainders[0] - k)>=1:
            count1 = d[remainders[0]]
            count2 = d[k - remainders[0]]
            if(count1>count2):
                newList = newList + [remainders[0]]*count1
            elif(count1<count2):
                newList = newList + [k - remainders[0]]*count2
            else:
                newList = newList + [remainders[0]]*count1
            remainders.remove(k-remainders[0])
            remainders.remove(remainders[0])
        elif(abs(2*remainders[0] - k)==0) or remainders[0]==0:
            newList = newList + [remainders[0]]
            remainders.remove(remainders[0])
        else:
            count3 = d[remainders[0]]
            newList = newList + [remainders[0]]*count3
            remainders.remove(remainders[0])
    print(newList)
    return len(newList)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()


# ref:

'''

https://www.hackerrank.com/challenges/non-divisible-subset/forum/comments/150647

https://www.hackerrank.com/challenges/non-divisible-subset/forum/comments/173323


Java: https://www.hackerrank.com/challenges/non-divisible-subset/forum/comments/545233


'''