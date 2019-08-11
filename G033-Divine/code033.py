# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 15:56:40 2019

@author: rvillareal
"""

import os
import sys

def checkTriple(mat, r, c, miss, swaps):
    # Check up
    if miss != 'U' and r >= 2:
        if mat[r - 2][c] == mat[r - 1][c] == mat[r][c]:
            return True
    # Check down
    if miss != 'D' and r <= 6:
        if mat[r][c] == mat[r + 1][c] == mat[r + 2][c]:
            return True
    # Check middle horizontal
    if (miss == 'U' or miss == 'D') and c > 0 and c < 8:
        if mat[r][c - 1] == mat[r][c] == mat[r][c + 1]:
            return True
    # Check left
    if miss != 'L' and c >= 2:
        if mat[r][c - 2] == mat[r][c - 1] == mat[r][c]:
            return True
    # Check right
    if miss != 'R' and c <= 6:
        if mat[r][c] == mat[r][c + 1] == mat[r][c + 2]:
            return True
    # Check middle vertical
    if (miss == 'L' or miss == 'R') and r > 0 and r < 8:
        if mat[r - 1][c] == mat[r][c] == mat[r + 1][c]:
            return True
    
    return False

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            mat = []
            for i in range(9):
                mat.append(fd.readline().rstrip('\n').split())

            r = 0
            c = 3
            swaps = []
            for r in range(9):
                for c in range(9):
                    # Swap right
                    if c < 8 and mat[r][c + 1] != mat[r][c]:
                        mat[r][c], mat[r][c + 1] = mat[r][c + 1], mat[r][c]
                        if (checkTriple(mat, r, c, 'R', swaps) or
                            checkTriple(mat, r, c + 1, 'L', swaps)):
                            swaps.append(" ".join([str(r), str(c),
                                                   str(r), str(c + 1)]))
                        mat[r][c], mat[r][c + 1] = mat[r][c + 1], mat[r][c]
                    # Swap down
                    if r < 8 and mat[r + 1][c] != mat[r][c]:
                        mat[r][c], mat[r + 1][c] = mat[r + 1][c], mat[r][c]
                        if (checkTriple(mat, r, c, 'D', swaps) or
                            checkTriple(mat, r + 1, c, 'U', swaps)):
                            swaps.append(" ".join([str(r), str(c),
                                                   str(r + 1), str(c)]))
                        mat[r][c], mat[r + 1][c] = mat[r + 1][c], mat[r][c]
            
            print(len(swaps))
            for swp in swaps:
                print(swp)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
