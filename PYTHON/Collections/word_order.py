
#WORD ORDER



# NEW ONE ==> referred from DISCUSSIONS

"""
Container
Return an instance of a dict subclass, supporting the usual dict methods. An OrderedDict is a dict that remembers the order that keys were first inserted. If a new entry overwrites an existing entry, the original insertion position is left unchanged. Deleting an entry and reinserting it will move it to the end.
New in version 3.1.

popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

move_to_end(key, last=True)
Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist:
Refer More : https://docs.python.org/3.6/library/collections.html#collections.OrderedDict
"""
"""
A Counter is a dict subclass for counting hashable objects. 
It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. 
Counts are allowed to be any integer value including zero or negative counts. 
The Counter class is similar to bags or multisets in other languages.
Refer more : https://docs.python.org/3.6/library/collections.html#collections.Counter
"""

# from collections import Counter, OrderedDict
# d = OrderedDict.fromkeys('abcde')
# print("".join(d))
# print(d.items())
# c = Counter(a=4, b=2, c=0, d=-2)
# print(c)
# print(sorted(c.elements()))



#Finally working one...referred from Discussion

from collections import Counter, OrderedDict
class OrderCounter(Counter, OrderedDict):
	pass
n = int(input())
l = OrderCounter(input() for i in range(n))
# print(l)
print(len(l))
print(*l.values())



