

# COLLECTIONS.ORDEREDDICT()






from collections import OrderedDict
n = int(input())
d = OrderedDict()
for _ in range(n):
    a = input().split()
    if(str(" ".join(a[:len(a)-1])) in d):
        d[str(" ".join(a[:len(a)-1]))]+=int(a[len(a)-1])
    else:
        d[str(" ".join(a[:len(a)-1]))] = int(a[len(a)-1])
        
for key, value in d.items(): 
    print(key, value) 


'''
#better soln..just not mine..  src:  hackerrank

from collections import OrderedDict
d = OrderedDict()
for _ in range(int(input())):
    item, space, quantity = input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for item, quantity in d.items():
    print(item, quantity)   


'''