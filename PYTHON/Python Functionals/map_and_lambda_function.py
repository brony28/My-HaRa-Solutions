
#MAP AND LAMBDA FUNCTION

cube = lambda x:pow(x,3) # complete the lambda function 
# def fibonacci(n):
#     i=0
#     j=1
    
#     if(n==0):
#         a=[]
#     elif(n==1):
#         a=[0]
#     else:
#         a=[0,1]
#         for _ in range(n-2):
#             k=i+j
#             a.append(k)
#             i=j
#             j=k
#     return a

def fibonacci(n):
    i=0
    j=1
    
    a=[0,1]
    for _ in range(n-2):
        k=i+j
        a.append(k)
        i=j
        j=k
    return a[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))