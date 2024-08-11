#   Carlos Paredes Márquez
#   Compare the triplets
#   Task: Given a and b, 
#   determine their respective comparison points.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    result = [0, 0]

    for i in range(len(a)):
        if (a[i] > b[i]):
            result[0] += 1
        elif (a[i] < b[i]):
            result[1] += 1
        else:
            continue
    
    return result


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(' '.join(map(str, result)))

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()

'''

Sample Input 0

5 6 7
3 6 10

Sample Output 0

1 1

'''