#EQUILIZE THE ARRAY

from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

a = Counter(arr)

# print()
print(sum(a.values()) - a.most_common(1)[0][1])

