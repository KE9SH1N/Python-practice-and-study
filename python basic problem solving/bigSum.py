import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    # Write your code here
    x = 0

    for i in ar:
        x = x+i
    return (x)


if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
