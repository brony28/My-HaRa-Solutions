#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the squares function below.
# def squares(a, b):
#     count = math.floor(math.sqrt(b))-math.ceil(math.sqrt(a))+1
#     return count


#It is called the Intermediate Value Theorem: https://en.wikipedia.org/wiki/Intermediate_value_theorem
'''Right. And it will work for projecting intervals from x to y using any function not just y= x^2 here 
an explanation I liked too https://www.youtube.com/watch?v=g9QRNbJLs94 thanks!
'''

        
# def squares(a,b):
#     count=0
#     while(a<=b):
#         if(str(math.sqrt(a))[-2:]=='.0'):
#             count+=1
#             a = (a//int(math.sqrt(a))+1)**2
#         else:
#             a+=1
#     return count


def squares(a,b):
    count=0
    val = 1
    while(val*val<a):
        val+=1
    while(val*val<=b):
        count+=1
        val = val+1
    return count

#Three diff solutions referred from Discussions.Couldnt solve myself :(
#Try using examples to understand the working of the algo.




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()


#ALSO check this out: Proper explanation:
#https://www.hackerrank.com/challenges/sherlock-and-squares/forum/comments/350423

#Without using import:
#https://www.hackerrank.com/challenges/sherlock-and-squares/forum/comments/434859