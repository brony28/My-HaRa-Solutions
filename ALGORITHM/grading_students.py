#GRADING STUDENTS

n = int(input())
for _ in range(n):
    a = int(input())
    if(a<38):
        pass
    elif(5-divmod(a,5)[1]<3):
        a=a+5-divmod(a,5)[1]
    print(a)
    