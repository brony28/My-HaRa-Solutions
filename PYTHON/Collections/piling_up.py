ans = []
t = int(input())
for _ in range(t):
    n = int(input())
    sl = list(map(int,input().split()))

    for _ in range(n-1):
        if(sl[0]>=sl[len(sl)-1]):
            a = sl[0]
            sl.pop(0)
        elif(sl[0]<sl[len(sl)-1]):
            a = sl[len(sl)-1]
            sl.pop(len(sl)-1)
        else:
            pass

        if(len(sl)==1):
            ans.append("Yes")
        # print(sl[0])
        # print(sl[len(sl)-1])
        # print("")    
        if((sl[0]>a) or (sl[len(sl)-1]>a)):
            ans.append("No")
            break
print("\n".join(ans))


#SOLVE THIS USING DEQUEUE!!!!!!!!