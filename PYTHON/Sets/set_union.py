
#SET UNION()  OPERATION



n = int(input())    
nn = set(map(int,input().split()))

b = int(input())
bb = set(map(int,input().split()))

c = sorted(nn.union(bb))
#sorted not reqd...

print(len(c))
# print(*c,sep="\n")

