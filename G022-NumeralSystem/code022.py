# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:02:32 2018

@author: rvillareal
"""

import os
import sys
import string

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            ec, z = fd.readline().rstrip('\n').split("=")
            x, y = ec.split("+")
            
            found = False
            letters = "0123456789" + string.ascii_uppercase
            b = letters.index(max([max(x), max(y), max(z)])) + 1
            while not found:
                if (int(x, base = b) + int(y, base = b)) == int(z, base = b):
                    found = True
                else:
                    b += 1
            
            print(b)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
