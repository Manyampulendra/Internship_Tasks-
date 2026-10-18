Problem 1:
Hackerank:https://www.hackerrank.com/challenges/py-if-else/copy-from/437820127
import math
import os
import random
import re
import sys
def check_weird(n):
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        else:  # n > 20
            print("Not Weird")

if __name__ == "__main__":
    n = int(input().strip())
    check_weird(n)
