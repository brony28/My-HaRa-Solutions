
#THE CAPTAIN'S ROOM


from collections import Counter

k = int(input()) #size of each grp
rno = list(map(int,input().split())) #room keys list
set_rno = set(rno) #set will store only the unique values

no_of_rno = len(rno) #will find the total room keys
no_of_fam = no_of_rno//k #this gives the no of families(e.g. 31//5 = 6)
#this no_of_fam will help to find the most common families having size of k

class hola(Counter):
    pass

comm_nos = hola(rno).most_common(no_of_fam)
#This finds the keys that are most common

a = set([i[0] for i in comm_nos]) 
#Counter stores the input as (key,value), So basically tuple inside list
#This for loop only takes the key part and stores in a list->a

print(*set_rno.difference(a))
#now set difference of rno and a will give captains key
#e.g. set_rno={1,2,3,4,5,6,8} ; a = {1,2,3,4,5,6} then set_rno.diff(a) will only give 8

