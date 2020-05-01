
#NO IDEA!  (sets)


n,m = map(int,input().split())
arr = list(map(int,input().split()))
m1,m2 = [set(map(int,input().split()))for _ in range(2)]

happy=0
for i in range(len(arr)):
    if(arr[i] in m1):
        happy+=1
    elif(arr[i] in m2):
        happy-=1
    else:
        pass
print(happy)

# print(n,m)
# print(arr)
# print(m1,m2,sep="\n")



# #cool soln incoming...just not mine....
# n, m = raw_input().split()
# sc_ar = raw_input().split()
# A = set(raw_input().split())
# B = set(raw_input().split())
# print sum([(i in A) - (i in B) for i in sc_ar])
# #it will simply create a list of 0's and 1's then sum will be taken.
# #it will check for each element in sc_ar, if it's present in A count will be incremented. 
# #Similarly in B, then count(A) and count(B) will be subtracted.

