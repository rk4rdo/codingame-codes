# -*- coding: utf-8 -*-
"""
@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            rots = [k for k in fd.readline().split()]
            srchFc = [fd.readline().rstrip()]
            srchFc.append(fd.readline().rstrip())
            
            wiseFaces = {'x': ['F', 'U', 'B', 'D'],
                         'y': ['F', 'L', 'B', 'R'],
                         'z': ['U', 'R', 'D', 'L']}
            for rot in rots:
                counter = True if len(rot) > 1 else False
                axis = rot[0]
                for iSrch in range(len(srchFc)):
                    if srchFc[iSrch] in wiseFaces[axis]:
                        pos = wiseFaces[axis].index(srchFc[iSrch])
                        if not counter:
                            pos = pos + 1 if pos + 1 < len(wiseFaces[axis]) else 0
                        else:
                            pos = pos -1 if pos - 1 >= 0 else len(wiseFaces[axis]) - 1
                        srchFc[iSrch] = wiseFaces[axis][pos]
            
            for fc in srchFc:
                print(fc)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
