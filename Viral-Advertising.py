import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    i=1
    k=5
    s=0
    while i<=n:
        a=abs(k//2)
        s=s+a
        day=a*3
        k=day
        i=i+1
    return s   


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
