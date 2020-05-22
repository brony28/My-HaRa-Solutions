

#Collections.deque()

from collections import deque
n = int(input())
l = [input().split() for i in range(n)]
# print(l)
d = deque()
for j in range(len(l)):
	if(len(l[j])==2):
		r = "d."+l[j][0]+"("+l[j][1]+")"
		eval(r)
	elif(len(l[j])==1):
		r = "d."+l[j][0]+"()"
		eval(r)

print(*d)


