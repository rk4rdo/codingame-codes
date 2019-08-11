# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:02:14 2018

@author: rvillareal
"""

import os
import sys

def numDigits(x):
    return len(str(x))

def sumDigits(x):
    return sum([int(k) for k in str(x)])

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            r_1 = int(fd.readline().rstrip())
            
            found = 0
            lowCap = r_1 - (9 * numDigits(r_1))
            allPossibles = range(r_1 - 1, lowCap if lowCap > 1 else 1, -1)
            for k in allPossibles:
                if k + sumDigits(k) == r_1:
                    found = k
                    break
            
            print("YES" if found != 0 else "NO")
#            print("Found: " + str(found))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
