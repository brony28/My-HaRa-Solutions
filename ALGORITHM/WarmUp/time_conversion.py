#TIME CONVERSION


def timeConversion(s):
    s1 = s.split(":")
    if(s1[2][2:]=="PM"):
        s1[2] = s1[2][:2]
        if(s1[0]=='12'):
            r = ":".join(s1)
        else:
            s1[0]=str(int(s1[0])+12)
            
            r = ":".join(s1)
    elif(s1[2][2:]=="AM" and s1[0]=='12'):
        s1[2] = s1[2][:2]
        s1[0]='00'
        r = ":".join(s1)
    elif(s1[2][2:]=="AM" and int(s1[0])>=1):
        s1[2] = s1[2][:2]
        r = ":".join(s1)

    return r


s = input()

result = timeConversion(s)
print(result)