

#CHECK SUBSET (sets)

'''
t = int(input())

for _ in range(t):
    nA = int(input())
    A = set(map(int,input().split()))
    nB = int(input())
    B = set(map(int,input().split()))

    print(A.issubset(B))

'''


t = int(input())
ans = []
for _ in range(t):
    nA = int(input())
    A = set(map(int,input().split()))
    nB = int(input())
    B = set(map(int,input().split()))

    ans.append(A.issubset(B))

print(*ans,sep="\n")


