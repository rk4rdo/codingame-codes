# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:02:46 2018

@author: rvillareal
"""

import os
import sys
from decimal import Decimal
from math import factorial, log10

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            n = int(fd.readline().rstrip())
            nums = [Decimal(k) for k in fd.readline().rstrip('\n').split()]
            
            sols = []
            for num in nums:
                k = 2 * int(num) - 1
                fK = factorial(k)
                rSide = log10(num)
                while rSide > (log10(fK) / k):
                    k += 1
                    fK *= k
                sols.append(str(k))
            
            print(" ".join(sols))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
