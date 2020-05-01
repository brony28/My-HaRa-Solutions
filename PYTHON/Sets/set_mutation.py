
#SET MUTATION (sets)



nA = int(input())
a = set(map(int,input().split()))

N = int(input())
for _ in range(N):
    comm,lenset = input().split()
    smallset = set(map(int,input().split()))

    if(comm == "update"):
        r = "a.update(smallset)"
        eval(r)
    elif(comm == "intersection_update"):
        r = "a.intersection_update(smallset)"
        eval(r)
    elif(comm == "symmetric_difference_update"):
        r = "a.symmetric_difference_update(smallset)"
        eval(r)
    elif(comm == "difference_update"):
        r = "a.difference_update(smallset)"
        eval(r)
print(sum(a))




"""
We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.
We can use the following operations to create mutations to a set:


.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])


.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.intersection_update(R)
>>> print H
set(['a', 'k'])


.difference_update() or -=
Update the set by removing elements found in an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.difference_update(R)
>>> print H
set(['c', 'e', 'H', 'r'])


.symmetric_difference_update() or ^=
Update the set by only keeping the elements found in either set, but not in both.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.symmetric_difference_update(R)
>>> print H
set(['c', 'e', 'H', 'n', 'r', 'R'])

"""