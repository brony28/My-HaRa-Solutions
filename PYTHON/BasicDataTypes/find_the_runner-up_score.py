#Find the Runner-Up Score


# b=[]
n = input()
# for i in range(int(n)):
#     a=input()
#     b.append(a)
b = map(int,input().split())

c=set(b)
b1=list(c)

b1.sort(reverse=True)

print(b1[1])