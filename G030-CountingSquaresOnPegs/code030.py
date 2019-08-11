# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 10:06:48 2018

@author: rvillareal
"""

import os
import sys

def getNumSquares(p1, coords):
    accum = 0
    for p2 in coords:
        xc = (p1[0] + p2[0]) / 2
        xd = (p1[0] - p2[0]) / 2
        yc = (p1[1] + p2[1]) / 2
        yd = (p1[1] - p2[1]) / 2
        q1 = ((xc - yd), (yc + xd))
        q2 = ((xc + yd), (yc - xd))
        if (not [k for k in q1 if k % 1 != 0] and
            not [k for k in q2 if k % 1 != 0]):
            if q1 in coords and q2 in coords:
#                print(" ".join(["Point", str(p1), str(p2), str(q1), str(q2)]))
                accum += 1
    return accum

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            n = int(fd.readline().rstrip())
            coords = set()
            for p in range(n):
                x, y = [int(k) for k in fd.readline().rstrip('\n').split()]
                coords.add((x, y))
            
            total = 0
            while coords:
                p = coords.pop()
                total += getNumSquares(p, coords)
            
            print(total)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
