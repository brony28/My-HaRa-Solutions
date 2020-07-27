
#!/bin/python3

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
       
    if(len(s)+len(t)<k):
        print("Yes")
    else:
        i=0 
        m = min( len(s), len(t) )
        while( i<m and s[i]==t[i]):
            # print(s[:i],t[:i])
            i+=1
        # stCommon = s[:i-1]
        # print(stCommon)
        toPopOutFromS = s[i:]
        toAppendToS = t[i:]
        # print(toPopOutFromS)
        # print(toAppendToS)
        st_sum = len(toPopOutFromS)+len(toAppendToS)
        if(k>=st_sum and st_sum%2==k%2):
            print("Yes")
        else:
            print("No")

s = input()
t = input()
k = int(input())
appendAndDelete(s, t, k)



'''
can you please explain diff%2==k%2 condition?

qwerasdf qwerzxcv 10 operations

substring qwer is the same in both strings, so diff = asdf+zxcv = 8,
 you need atleast 8 operations 
to create the required string(delete asdf and append zxcv).But then 
if they gave you exactly two more 
operations to work with (10), you could remove 'r' from qwer and then
 append it. If they gave you 12 
you could do the same thing to 'e'...



Essentially checks to see if the difference between the two strings are odd and that k is odd. 
If this is the case, it is trivial to see that an even number 
of appends/deletions can be made to make the strings equal :)

https://www.hackerrank.com/challenges/append-and-delete/forum/comments/310810


VVImp
https://www.hackerrank.com/challenges/append-and-delete/forum/comments/709151

'''