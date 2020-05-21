
#ginortS


s = input()

small=[]
cap=[]
numodd=[]
numeven=[]

for i in sorted(s,key=lambda x:ord(x)):
    if(i.isupper()):
        cap.append(i)
    elif(i.islower()):
        small.append(i)
    elif(i.isdigit()):
        if(int(i)%2!=0):
            numodd.append(i)
        else:
            numeven.append(i)        
print("".join(small+cap+numodd+numeven))



'''
#ANOTHER SOLN...just not mine
def getKey(x):
    if x.islower():
        return(1,x)
    elif x.isupper():
        return(2,x)
    elif x.isdigit() :
        if int(x)%2==1:
            return(3,x)
        else :
            return(4,x)

print(*sorted(input(),key=getKey),sep='')

'''


