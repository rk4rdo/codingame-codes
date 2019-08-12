#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:20:43 2019

@author: zokk
"""

import os
import sys

def calcMaxRoute(k):
    if k in infl:
        maxWay = 0
        for neigh in infl[k]:
            actWay = 1 + calcMaxRoute(neigh)
            maxWay = actWay if actWay > maxWay else maxWay
        return maxWay
    else:
        return 1

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            infl = {}
            n = int(fd.readline().rstrip('\n'))  # Number of relationships
            for i in range(n):
                # Relationship of influence between two people (x influences y)
                x, y = [int(j) for j in fd.readline().rstrip('\n').split()]
                if x in infl:
                    infl[x].append(y)
                else:
                    infl[x] = [y]
            
            maxR = 0
            for ind in infl:
                actR = calcMaxRoute(ind)
                maxR = actR if actR > maxR else maxR
            
            print(maxR)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
