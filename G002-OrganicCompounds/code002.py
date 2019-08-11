# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 17:34:27 2018

@author: rvillareal
"""

import os
import sys

def isC(allMols, k, q):
    if k >= 0 and k < len(allMols) and q >= 0 and q < len(allMols[k]):
#        print("k =", k)
#        print("q =", q)
#        print("Checking =", allMols[k][q])
        return True if allMols[k][q].startswith('C') else False
    return False

def isB(allMols, k, q):
    if k >= 0 and k < len(allMols) and q >= 0 and q < len(allMols[k]):
        return True if allMols[k][q].startswith('(') else False
    return False

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            n = int(fd.readline().rstrip())
            
            allMols = []
            for k in range(n):
                compound = fd.readline().rstrip('\n')
                mols = [compound[i:i + 3] for i in range(0, len(compound), 3)]
                allMols.append(mols)
            
#            print(allMols)
            
            valid = True
            for k in range(n):
                for q in range(len(allMols[k])):
                    if isC(allMols, k, q):
#                        print(allMols[k][q], "is carbon with",
#                              allMols[k][q][2], "hydrogen mols")
                        valence = int(allMols[k][q][2])
#                        print("Valence = " + str(valence))
                        for neigh in [(k + 1, q), (k, q + 1),
                                          (k - 1, q), (k, q - 1)]:
                            if isC(allMols, neigh[0], neigh[1]):
#                                print("M =",
#                                      allMols[neigh[0]][neigh[1]])
                                valence += int(allMols[neigh[0]][neigh[1]][2])
#                                print("Add mol valence = " + str(valence))
                            elif isB(allMols, neigh[0], neigh[1]):
#                                print("B =",
#                                      allMols[neigh[0]][neigh[1]])
                                valence += int(allMols[neigh[0]][neigh[1]][1])
#                                print("Add bond valence = " + str(valence))
                        if valence != 4:
#                            print("Not valid sequence")
                            valid = False
                            break
#                    elif isB(allMols, k, q):
#                        print(allMols[k][q] + " is bond")
#                    else:
#                        print(allMols[k][q] + " is empty")
            
            print("VALID" if valid else "INVALID")
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
