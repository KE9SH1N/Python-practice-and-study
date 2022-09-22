import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#


#data = []
#n = int(input('Enter how many elements you want: '))
#for i in range(0, n):
#x = input('Enter the numbers into the array: ')
#data.append(x)
#print(data)


def simpleArraySum(ar):
    sum = 0

    for i in ar:
        sum = sum+i
    return (sum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
