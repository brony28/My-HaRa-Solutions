#APPLE AND ORANGE

def countappora(li,j):
    count = 0
    for i in li:
        if(i+j>=s and i+j<=t):
            count+=1
    return count

s,t = map(int,input().split())
a,b = map(int,input().split())
m,n = map(int,input().split())
app = list(map(int,input().split()))
ora = list(map(int,input().split()))


print(countappora(app,a))
print(countappora(ora,b))




# #another super code/......just not mine...

# print(sum([1 for x in apple if (x + a) >= s and (x + a) <= t]))
# print(sum([1 for x in orange if (x + b) >= s and (x + b) <= t]))


#Another awesome code...not mine...

# You can also use the fact that True == 1 and False == 0
# print(sum(s <= a + d <= t for d in apples))
# print(sum(s <= b + d <= t for d in oranges))