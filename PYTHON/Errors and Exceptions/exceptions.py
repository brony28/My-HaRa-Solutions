#EXCEPTIONS

t = int(input())
for _ in range(t):
    val=input().split()
    try:
        print(int(val[0])//int(val[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)




#another soln...just not mine..
'''

Or instead of "Exception", you can simply use "BaseException" since it's the base class for all built-in exceptions (and "Exception" actually inherits from "BaseException") as below :

for i in range(int(input())):  
    try:
        a,b= map(int,input().split())
        print(a//b)
    except BaseException as e:
        print("Error Code:",e)

'''