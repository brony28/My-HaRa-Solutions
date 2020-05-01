
#SET.SYMMETRIC DIFFERENCE 


n = int(input())
n1 = input().split()
m = int(input())
m1 = input().split()

n2 = set(n1)
m2 = set(m1)

final = n2.symmetric_difference(m2)
final1 = list(final)
print(len(final1))


