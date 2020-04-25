m=[]
n = int(input("Enter the count"))
for i in range(n):
	print("Entry no "+str(i+1)+"=>>")
	n2=[]
	for j in range(2): #only 2 parameters taken name and marks
		n1=input("Enter value :")
		n2.append(n1)
	print(n2) #Individual lists
	
	m.append(n2)
print(m) #Nested list



y=[]
for x in m: # "x" will take each individual list
	y.append(x[1]) # x[0] -> name, x[1] -> marks
print(y) #stored and printed only marks of students

y1=set(y) #converted list "y" to set
y2=list(y1) #converted back set y1 to y2
#used Set to store 'unique values' in the newly created list "y2"

y2.sort(key=float) #sorting the list, which will help to find the 2nd least mark
print(y2) 

z1=[]
for z in m: #scanning each individual list(z) in the nested list m
	if float(z[1])==float(y2[1]): #y2[1] contains 2nd least value and is compared with z to find the names with those marks,
									#z[0]-> names, z[1]->marks
		print(z[0]) #just printing those name....tp :P
		z1.append(z[0]) #storing the names into a new list

z1.sort() #sorting the new list 
print()
print()
for r in z1:
	print(r) #printing the names



###############################################

#HackerRank format:

"""
m=[]
n = int(input())
for i in range(n):
    
    n2=[]
    for j in range(2): #only 2 parameters taken name and marks
        n1=input()
        n2.append(n1)    
    m.append(n2)


y=[]
for x in m: # "x" will take each individual list
    y.append(x[1]) # x[0] -> name, x[1] -> marks
#y has all the marks list
y1=set(y) #converted list "y" to set
y2=list(y1) #converted back set y1 to y2
y2.sort(key=float) #sorting the list, which will help to find the 2nd least mark


z1=[]
for z in m: #scanning each individual list(z) in the nested list m
    if float(z[1])==float(y2[1]): 
z1.sort() #sorting the new list 


for r in z1:
    print(r) #printing the names

"""




