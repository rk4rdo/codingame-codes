# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 12:18:30 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            np = int(fd.readline())
            poly = []
            for p in range(np):
                poly.append([int(k) for k in fd.readline().split()])
            ns = int(fd.readline())

            for s in range(ns):
                x, y = [int(k) for k in fd.readline().split()]
                pos = neg = 0
                for p in range(np):
                    px1, py1 = poly[p]
                    if px1 == x and py1 == y:
                        pos = neg = 0
                        break
                    nxp = p + 1 if p + 1 < np else 0
                    px2, py2 = poly[nxp]
                    
                    d = (x - px1) * (py2 - py1) - (y - py1) * (px2 - px1)
                    if d > 0:
                        pos += 1
                    elif d < 0:
                        neg += 1
                print("miss" if pos > 0 and neg > 0 else "hit")
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
