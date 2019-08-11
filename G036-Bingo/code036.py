# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 10:33:19 2019

@author: rvillareal
"""

import os
import sys

NLINE = 5
DRGHT = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
DLEFT = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]

def checkLine(marked, c, l, e):
    # Check horizontal
    line = True if sum(marked[c][l]) == 5 else False
    # Check vertical
    if not line:
        line = True if sum([ln[e] for ln in marked[c]]) == 5 else False
        # Check diagonal right
        if not line and l == e:
            sumDR = sum([marked[c][d1][d2] for d1, d2 in DRGHT])
            line = True if sumDR == 5 else False
        # Check diagonal left
        if not line and (l, e) in DLEFT:
            sumDL = sum([marked[c][d1][d2] for d1, d2 in DLEFT])
            line = True if sumDL == 5 else False
    
    return line

def checkBingo(marked, c):
    return True if sum([sum(ln) for ln in marked[c]]) == 25 else False

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            tLine = -1
            tBingo = -1
            cards = []
            marked = []
            nP = int(fd.readline().rstrip())
            for p in range(nP):
                beg = NLINE * (p - 1)
                cards.append([])
                marked.append([])
                for l in range(NLINE):
                    cards[p].append(fd.readline().rstrip().split())
                    if l != 2:
                        cardRow = [False] * NLINE
                        marked[p].append(cardRow)
                    else:
                        cardRow = [False if q != 2 else True for q in range(5)]
                        marked[p].append(cardRow)
            
            k = 0
            for n in fd.readline().rstrip().split():
                k += 1
#                print("Checking " + n)
                for c in range(len(cards)):
#                    print("Checking card " + str(c))
                    found = False
                    for l in range(NLINE):
                        for e in range(len(cards[c][l])):
                            if n == cards[c][l][e]:
                                marked[c][l][e] = True
                                found = True
                                if tLine < 0 and checkLine(marked, c, l, e):
                                    tLine = k
                                if tBingo < 0 and checkBingo(marked, c):
                                    tBingo = k
                                break
                        if found:
                            break
                    if tLine >= 0 and tBingo >= 0:
                        break
                if tLine >= 0 and tBingo >= 0:
                    break
            
            print(tLine)
            print(tBingo)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
