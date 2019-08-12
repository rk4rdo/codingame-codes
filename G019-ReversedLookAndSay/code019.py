# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:03:06 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            s = fd.readline().rstrip('\n')
            
            fact = True
            while fact:
                if len(s) % 2 == 0:
                    # Define new num. and last num.
                    nextNum = ""
                    lastNum = 10
            
                    elems = list(map(''.join, zip(*[iter(s)]*2)))
                    for e in elems:
                        x, y = [int(k) for k in e]
                        if y != lastNum:
                            lastNum = y
                            nextNum += x * str(y)
                        else:
                            fact = False
                            break
                    
                    if nextNum == s:
                        fact = False
                    else:
                        s = nextNum if fact else s
                else:
                    fact = False
            
            print(s)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
