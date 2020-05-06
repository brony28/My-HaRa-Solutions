#COMPRESS THE STRING!




from itertools import groupby

text = input()

for i,j in groupby(text,lambda x:x[0]):
	# print(len(list(j)),i)
	print(f'({len(list(j))},{i})',end=' ')


OR


# from itertools import groupby
# text = input()

# print(*[ (len(list(j)),int(i)) for i,j in groupby(text)])




