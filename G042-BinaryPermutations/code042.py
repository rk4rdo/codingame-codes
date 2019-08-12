#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:36:07 2019

@author: zokk
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            nb, nc = [int(k) for k in fd.readline().rstrip('\n').split()]
            lIn = ['' for k in range(nb)]
            lOut = ['' for k in range(nb)]
            fNum = '0' + str(nb) + 'b'
            
            for c in range(nc):
                x, y = [int(k) for k in fd.readline().rstrip('\n').split()]
                xIn = list(format(x, fNum))
                lIn = [lIn[k] + xIn[k] for k in range(nb)]
                yOut = list(format(y, fNum))
                lOut = [lOut[k] + yOut[k] for k in range(nb)]
            
            dPerm = {}
            for k in range(nb):
                dPerm[lOut.index(lIn[k])] = k
            
            res = []
            for k in range(nb):
                xIn = list(format(2**k, fNum))
                yOut = ''
                for q in range(nb):
                    yOut += xIn[dPerm[q]]
                res.append(int(yOut, 2))
            
            print(" ".join([str(k) for k in res]))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
