

#ATHLETE SORT



n,m  = map(int,input().split())
excel=[]
for _ in range(n):
    excel.append(list(map(int,input().split())))
k = int(input())

for i in sorted(excel,key=lambda x:x[k]):
    print(*i)







