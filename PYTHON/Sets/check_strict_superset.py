
#CHECK STRICT SUPERSET


A = set(map(int,input().split()))
N = int(input())
cond = True
for _ in range(N):
    
    Nn = set(map(int,input().split()))
    if(A.issuperset(Nn)==False):
        cond = False
        break
print(cond)



"""
You are given a set  and  other sets.
Your job is to find whether set  is a strict superset of each of the  sets.

Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example
Set is a strict superset of set.
Set is not a strict superset of set.
Set is not a strict superset of set.
"""