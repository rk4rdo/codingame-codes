# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:47:26 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            w, h = [int(k) for k in fd.readline().split()]
            labels = {}
            iRow = fd.readline()
            origOrder = iRow.split()
            for k in range(len(iRow)):
                if iRow[k] in origOrder:
                    labels[iRow[k]] = k
            
            for r in range(1, h - 1):
                row = fd.readline()
                for lab in labels:
                    pos = labels[lab]
                    if pos + 1 < len(row) and row[pos + 1] == "-":
                        pos += 1
                        while row[pos] != "|":
                            pos += 1
                    elif pos - 1 >= 0 and row[pos - 1] == "-":
                        pos -= 1
                        while row[pos] != "|":
                            pos -= 1
                    labels[lab] = pos
            
            eRow = fd.readline()
            for lab in origOrder:
                print(lab + eRow[labels[lab]])
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)








