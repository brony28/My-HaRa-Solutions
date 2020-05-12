


#COLLECTIONS.COUNTER()

'''
from collections import Counter
x = int(input())
xsize = Counter(list(map(int,input().split())))
n = int(input())

# print(xsize)
sum = 0
for _ in range(n):
    size,price = map(int,input().split())
    if(xsize[size]):
        sum+=price
        xsize.subtract(Counter([size])) #xsize[size] -= 1
        # print(xsize[size])
print(sum)

'''
#without counter

'''
from collections import Counter
x = int(input())
xsize = list(map(int,input().split()))
n = int(input())

sum = 0
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0] in xsize:
	    sum =sum + a[1]
	    xsize.remove(a[0])

print(sum)

# But here .remove performs sequential search, hence takes more time to execute.. While Counter searches the hash value and is faster.

'''
