# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:31:17 2018

@author: rvillareal
"""

import os
import sys

def getNumNodes(nodes):
    return sum([getNumNodes(nodes[k]) + 1 for k in nodes])

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            phones = {}
            nTel = int(fd.readline().rstrip('\n'))
            k = 1
            for k in range(nTel):
                phn = fd.readline().rstrip('\n')
                nextNode = phones
                while phn:
                    num = int(phn[0])
                    if num not in nextNode:
                        nextNode[num] = {}
                    nextNode = nextNode[num]
                    phn = phn[1:]
            
            print(getNumNodes(phones))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
