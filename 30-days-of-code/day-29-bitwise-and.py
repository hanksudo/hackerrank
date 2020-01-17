# https://www.hackerrank.com/challenges/30-bitwise-and/forum/comments/163404

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = 3
    for t_itr in range(t):
        nk = ["5 2", "8 5", "2 2"][t_itr].split()
        n = int(nk[0])
        k = int(nk[1])

        print(k - 1 if ((k - 1) | k) <= n else k - 2)
