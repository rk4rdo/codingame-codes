# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:56:06 2018

@author: rvillareal
"""

import os
import sys
import numpy as np

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            sc = int(fd.readline())
            
            allCombinations = []
            start = [0, 0, 0]
            
            def bt(sc, comb, allCombinations, ind = 0):
                pnt = (5, 2, 3)
                curr = sum(np.multiply(pnt, comb))
                if curr == sc and comb[1] <= comb[0]:
                    allCombinations.append(comb)
                elif curr < sc:
                    for k in range(ind, len(pnt)):
                        nComb = comb[:]
                        nComb[k] += 1
                        bt(sc, nComb, allCombinations, k)
            
            bt(sc, start, allCombinations)
            
            allCombinations = sorted(allCombinations)
            for comb in allCombinations:
                print(" ".join([str(x) for x in comb]))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
