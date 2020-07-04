#BON APPETIT

n,k = map(int,input().split())
bill = list(map(int,input().split()))
b = int(input())

bill.pop(k)
if(sum(bill)/2!=b):
    print(b-int(sum(bill)/2))
else:
    print("Bon Appetit")