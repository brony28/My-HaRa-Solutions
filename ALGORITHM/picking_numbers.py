#PICKING NUMBERS

n=int(input())
l=[int(i) for i in input().split()]
maxi=[]
for i in l:
    c=l.count(i)
    d=l.count(i-1)
    maxi.append(c+d)
print(max(maxi))

#Reference:
# https://www.hackerrank.com/challenges/picking-numbers/forum/comments/790431


# https://www.hackerrank.com/challenges/picking-numbers/forum/comments/841702

	