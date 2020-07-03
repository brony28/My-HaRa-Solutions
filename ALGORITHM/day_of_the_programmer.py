#DAY OF THE PROGRAMMER

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):

    if(year<=1917):
        return '12.09.%s' %year if(year%4==0) else '13.09.%s' %year
    elif(year>=1919):
        return '12.09.%s' %year if(year%400==0 or (year%4==0 and year%100!=0)) else '13.09.%s' %year
    else:
        return '26.09.%s' %year

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
