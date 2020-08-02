#CUT THE STICKS


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    stickCut=[]
    while(len(arr)!=0):
        minVal = min(arr)
        count = sum((i-minVal)>=0 for i in arr)
        arr = [i-minVal for i in arr if(i-minVal!=0)]
        stickCut.append(count)
        # print(arr)
        # print(count)

        # stickCut.append(len(arr))
        # minVal = min(arr)
        # arr = [i-minVal for i in arr if(i-minVal!=0)]
    return stickCut


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()



#Java Implementation:
'''

import java.util.Scanner;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        /* Save Input */
        Scanner scan = new Scanner(System.in);
        int numSticks = scan.nextInt();
        int [] array = new int[numSticks];
        for (int i = 0; i < numSticks; i++) {
            array[i] = scan.nextInt();
        }
        scan.close();
        
        Arrays.sort(array);
        
        System.out.println(array.length);
        for (int i = 1; i < array.length; i++) {
            if (array[i] != array[i-1]) {
                System.out.println(array.length - i);
            }
        }
    }
}


https://www.hackerrank.com/challenges/cut-the-sticks/forum/comments/274031

'''