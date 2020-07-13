#DESIGNER PDF VIEWER


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):

    maxofword = max(h[ord(word[i])-97] for i in range(len(word))) # max fun with list comprehension; ord() : gives the ascii value of character
    return len(word)*maxofword



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
