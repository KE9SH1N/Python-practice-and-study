

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    # Write your code here
    x = 0
    y = 0
    for i in range(0, len(arr)):
        x += arr[i][i]
        y += arr[i][len(arr)-i-1]

    sum = 0
    sum = abs(x-y)
    print(sum)


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    #fptr.write(str(result) + '\n')

    #fptr.close()
