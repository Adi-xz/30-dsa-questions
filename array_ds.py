import math

import random

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
        c=""
        for i in a[::-1]:
            c+=str(i)+" "
        print(c)

if __name__ == '__main__':
   

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

  
