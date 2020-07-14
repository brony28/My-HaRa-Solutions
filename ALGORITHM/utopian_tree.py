#UTOPIAN TREE


t = int(input())
for _ in range(t):
    period = int(input())
    height = 1
    for i in range(1,period+1):
        if(i%2==0):
            height+=1
        else:
            height*=2
    print(height)

