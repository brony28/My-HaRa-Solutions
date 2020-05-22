

#COMPANY LOGO
from collections import Counter, OrderedDict #OrderedDict not necessary...Counter is enough
class hola(Counter,OrderedDict):
	pass
a = hola(sorted(input())).most_common(3)  #sorted : sorts based on key value(in our case its alphabets)
#hola : takes all the properties of Counter(inheritance)
#.most_common() : gives the 3 most commonly occured alphabets based on count of each of them
[print(*i) for i in a]
#since its tuple inside list...Using for loop to iterate and display the value..* removes all the brackets and commas


