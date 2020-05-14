
# COLLECTIONS.NAMEDTUPLE()


from collections import namedtuple

n = int(input())
column = input().split()
sum = 0
Student = namedtuple('Student',column)
for _ in range(n):
    r = Student._make(input().split())
    sum+=int(r.MARKS)
print(sum/n)




'''

Basically, namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

Example

Code 01

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

Code 02

>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

Code 03

>>> Name = nametuple('Name','Age,Gender,Mood,Skills')
>>> r = Name(20,'M','Depressed',0)
>>> r
Name(Age=20, Gender='M', Mood='Depressed', Skills=0)
>>> r.Age
20
>>> b = Name(Gender='M',Skills=9,Age=100,Mood='Happy')
>>> b
Name(Age=100, Gender='M', Mood='Happy', Skills=9)



'''