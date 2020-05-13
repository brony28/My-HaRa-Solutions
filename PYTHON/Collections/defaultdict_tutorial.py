
# DEFAULTDICT TUTORIAL





#WORKING CODE
from collections import defaultdict
d = defaultdict(list)

n,m = map(int,input().split())

for i in range(n):
    d[input()].append(i+1)

ml = [input() for j in range(m)]

for i in ml:
    if i in d.keys():
        print(*d[i])
    else:
        print(-1)





'''

from collections import defaultdict
d = defaultdict(list)

n,m = map(int,input().split())
nl = [input() for _ in range(n)]
ml = [input() for _ in range(m)]



for i in ml:
    if i not in nl:
        d[i].append(-1)
    else:
        for j in range(len(nl)):
            if(i==nl[j]):
                d[i].append(j+1)
        

for r in d.values():
    print(*r)
# 3 test cases failed...reason : UNKNOWN
'''

