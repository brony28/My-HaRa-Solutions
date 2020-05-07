

#ITERABLES AND ITERATORS

from itertools import combinations
n = int(input())
nlist = input().split()
k = int(input())

c1 = len(list(combinations(nlist,k)))

c2 = len([i for i in list(combinations(nlist,k)) if('a' in i)])
print(round(c2/c1,3))


