
di={}
n = int(input()) #no of iterations

for i in range(n):
	a = input().split() #takes the value with spaces..and splits them and stores in the form of list
	di[a[0]]=list(map(float,a[1:])) #mapping key with value 
print(di)
m = str(input()) 

for key,value in di.items(): #traverse through the dict
	if(m==str(key)):
		per=list(value) #storing the values in to a list "per"
print(per)
print('%.2f' %(sum(per)/len(per)))



#############################################


#HackerRank supported


di={}
n = int(input()) #no of iterations

for i in range(n):
    a = input().split() #takes the value with spaces..and splits them and stores in the form of list
    di[a[0]]=list(map(float,a[1:])) #mapping key with value 

m = str(input()) 

for key,value in di.items(): #traverse through the dict
    if(m==str(key)):
        per=list(value) #storing the values in to a list "per"

print('%.2f' %(sum(per)/len(per)))




