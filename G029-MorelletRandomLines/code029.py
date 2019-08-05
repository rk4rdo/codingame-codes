# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:11:58 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            pX, pY, qX, qY = [int(k) for k in fd.readline().split()]
            nL = int(fd.readline())
            
            allLns = []
            cuts = 0
            onLine = False
            ln = 0
            for ln in range(nL):
                a, b, c = [int(k) for k in fd.readline().split()]
                cL = (a, b, c)
                if cL not in allLns:
                    # Check if line is unique
                    memCL = [k for k in range(3) if cL[k] != 0]
                    added = False
                    for pL in allLns:
                        # Check
                        memPL = [k for k in range(3) if pL[k] != 0]
                        if memCL == memPL:
                            aL = set([cL[k] / pL[k]
                                        for k in range(3) if pL[k] != 0])
                            if len(aL) == 1:
                                added = True
                                break
                    if not added:
                        allLns.append(cL)
                        pVal = a * pX + b * pY + c
                        qVal = a * qX + b * qY + c
                        if pVal == 0 or qVal == 0:
                            onLine = True
                            break
                        else:
                            # Check if line is between points
                            if ((pVal < 0 and qVal > 0) or
                                    (pVal > 0 and qVal < 0)):
                                cuts += 1
            
            if onLine:
                print("ON A LINE")
            else:
                print("YES" if cuts % 2 == 0 else "NO")
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)






