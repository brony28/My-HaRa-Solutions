#LISTS (basic data type)


l=[]
n = int(input())
for i in range(n):
    a = input().split()
    if(len(a)==1):
        # print("pop,print,sort,reverse")
        if(str(a[0])=='print'):
            print(l)
        else:
            r = "l."+str(a[0])+"()"
            eval(r)    
    elif(len(a)==2):
        # print("remove,append")
        r = "l."+str(a[0])+"("+str(a[1])+")"
        eval(r)
    else:
        # print("insert")
        r = "l.insert("+str(a[1])+","+str(a[2])+")"
        eval(r)
# print(l)