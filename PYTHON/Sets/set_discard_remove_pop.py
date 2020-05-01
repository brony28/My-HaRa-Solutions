
#SET DISCARD(), REMOVE() AND POP()




"""
remove(x)
This operation removes element  from the set.
If element  does not exist, it raises a KeyError.
The .remove(x) operation returns None.

Example
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.remove(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.remove(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.remove(0)
KeyError: 0


.discard(x)
This operation also removes element  from the set.
If element  does not exist, it does not raise a KeyError.
The .discard(x) operation returns None.

Example
>>> s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> s.discard(5)
>>> print s
set([1, 2, 3, 4, 6, 7, 8, 9])
>>> print s.discard(4)
None
>>> print s
set([1, 2, 3, 6, 7, 8, 9])
>>> s.discard(0)
>>> print s
set([1, 2, 3, 6, 7, 8, 9])


.pop()
This operation removes and return an arbitrary element from the set.
If there are no elements to remove, it raises a KeyError.

Example
>>> s = set([1])
>>> print s.pop()
1
>>> print s
set([])
>>> print s.pop()
KeyError: pop from an empty set
"""






#Using eval is not recommended in prog lang..


n = int(input())
s = set(map(int, input().split()))

N = int(input())
commands=[]
for _ in range(N):
    commands.append(input().split())

for i in commands:
    if("pop" in i):
        r = "s.pop()"
        eval(r)
        # print(s)
    elif("remove" in i):
        r = "s.remove(int(i[1]))"
        eval(r)
        # print(s)
    elif("discard" in i):
        r = "s.discard(int(i[1]))"
        eval(r)
        # print(s)
print(sum(s)) 



#So onto better one ...> getattr

#MAYBE A LITTLE LATER >> i AM SLEEPY RYT NOW >>> ITS 6.46 am and I havent slept yet....
