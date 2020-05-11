
#MAXIMIZE IT



from itertools import product

Ni = []
k,M = map(int,input().split())
for _ in range(k):
    Ni.append(list(map(int,input().split()))[1:])
# print(Ni)
# print(*Ni)
# print(list(product(*Ni)))
NiList = list(product(*Ni))

sumilist=[]
for x in NiList:
    sumi=0
    for y in x:
        sumi = pow(y,2)+sumi
    sumilist.append(sumi)
# print(sumilist)

sumilist = [i%M for i in sumilist]
# print(sumilist)

print(max(sumilist))

