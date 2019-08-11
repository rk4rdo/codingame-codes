# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:12:45 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            opBowls = [int(k) for k in fd.readline().split()]
            myBowls = [int(k) for k in fd.readline().split()]
            k = int(fd.readline())
            
            isMyBowls = True
            goBowls = myBowls
            v = goBowls[k]
            goBowls[k] = 0
            while v != 0:
                k += 1
                if k == len(goBowls):
                    k = 0
                    goBowls = opBowls if isMyBowls else myBowls
                    isMyBowls = False if isMyBowls else True
            
                if k != (len(goBowls) - 1) or isMyBowls:
                    goBowls[k] += 1
                    v -= 1
            
            showop = " ".join(str(x) for x in opBowls[:-1])
            showmy =  " ".join(str(x) for x in myBowls[:-1])
            print(showop, "[" + str(opBowls[-1]) + "]")
            print(showmy, "[" + str(myBowls[-1]) + "]")
            if k == (len(goBowls) - 1) and isMyBowls:
                print("REPLAY")
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
