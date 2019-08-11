# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 18:04:38 2019

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            nR = int(fd.readline())
            nV = int(fd.readline())
            tRobber = {k:0 for k in range(nR)}
            for v in range(nV):
                r = min(tRobber, key = tRobber.get)
                nC, nD = [int(k) for k in fd.readline().split()]
                tRobber[r] += (10**nD) * (5**(nC - nD))
            
            print(tRobber[max(tRobber, key = tRobber.get)])
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
