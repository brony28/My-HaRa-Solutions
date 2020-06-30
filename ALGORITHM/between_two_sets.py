#BETWEEN TWO SETS


#https://www.hackerrank.com/challenges/between-two-sets/forum/comments/490749

from functools import reduce
from math import gcd
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def lcm(a,b):
    return int((a*b)/gcd(a,b))

lcma = reduce(lcm,a)
gcdb = int(reduce(gcd,b))

# factors = [lcma*i for i in range(1,110) if(lcma*i)<=gcdb]
factors = range(lcma,gcdb+1,lcma)
# print(factors)

# count = 0
# for i in factors:
#     if(gcdb%i==0):
#         count+=1
# print(count)

print(sum(gcdb%i==0 for i in factors))

