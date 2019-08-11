#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:43:28 2019

@author: zokk
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            m = int(fd.readline().rstrip())
            n = int(fd.readline().rstrip())
            chart = []
            for i in range(m):
                chart.append([int(k) for k in fd.readline().rstrip()])
            
#            print(chart, file = sys.stderr)
            
            def rec(chart, x, y):
                if x == (m - 1) and y == (n - 1):
                    return 1
                else:
                    t = 0
                    if x + 1 < m:
                        if chart[x + 1][y] == 0:
                            t += rec(chart, x + 1, y)
                    if y + 1 < n:
                        if chart[x][y + 1] == 0:
                            t += rec(chart, x, y + 1)
                    return t
            
            print(rec(chart, 0, 0))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
