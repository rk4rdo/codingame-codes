# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:53:26 2018

@author: rvillareal
"""

import os
import sys

def markWord(marked, r, c, re, ce):
    if r == re:
        for z in range(c, ce):
            marked[r][z] = True
    elif c == ce:
        for y in range(r, re):
            marked[y][c] = True
    else:
        rangeR = range(r, re) if r <= re else range(re, r)
        rangeR = reversed(rangeR) if r > re else rangeR
        rangeC = range(c, ce) if c <= ce else range(ce, c)
        rangeC = reversed(rangeC) if c > ce else rangeC
        for y, z in zip(rangeR, rangeC):
            marked[y][z] = True

def getHF(r, c, grid):
    return ''.join([v for k, v in grid[r].items() if k >= c])
def getHR(r, c, grid):
    return ''.join([v for k, v in grid[r].items() if k <= c])[::-1]
def getVU(r, c, grid):
    return ''.join([v[c] for k, v in grid.items() if k <= r])[::-1]
def getVD(r, c, grid):
    return ''.join([v[c] for k, v in grid.items() if k >= r])
def getDDF(r, c, grid):
    return ''.join([grid[x][y] for x, y in
            zip(range(r, len(grid)), range(c, len(grid[r])))])
def getDDR(r, c, grid):
    return ''.join([grid[x][y] for x, y in
            zip(range(r, len(grid)), reversed(range(c + 1)))])
def getDUF(r, c, grid):
    return ''.join([grid[x][y] for x, y in
            zip(reversed(range(r + 1)), range(c, len(grid[r])))])
def getDUR(r, c, grid):
    return ''.join([grid[x][y] for x, y in
            zip(reversed(range(r + 1)), reversed(range(c + 1)))])

def searchWord(wrd, grid):
    for r in range(len(grid)):
        for c in range(len(grid)):
            if grid[r][c] == wrd[0]:
                if getHF(r, c, grid).startswith(wrd):
                    markWord(marked, r, c, r, c + len(wrd))
                    break
                if getHR(r, c, grid).startswith(wrd):
                    markWord(marked, r, c - len(wrd) + 1, r, c + 1)
                    break
                if getVU(r, c, grid).startswith(wrd):
                    markWord(marked, r - len(wrd) + 1, c, r + 1, c)
                    break
                if getVD(r, c, grid).startswith(wrd):
                    markWord(marked, r, c, r + len(wrd), c)
                    break
                if getDDF(r, c, grid).startswith(wrd):
                    markWord(marked, r, c, r + len(wrd), c + len(wrd))
                    break
                if getDDR(r, c, grid).startswith(wrd):
                    markWord(marked, r, c + 1, r + len(wrd), c - len(wrd) + 1)
                    break
                if getDUF(r, c, grid).startswith(wrd):
                    markWord(marked, r + 1, c, r - len(wrd) + 1, c + len(wrd))
                    break
                if getDUR(r, c, grid).startswith(wrd):
                    markWord(marked, r + 1, c + 1,
                                     r - len(wrd) + 1, c - len(wrd) + 1)
                    break

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            lWords = []
            n = int(fd.readline().rstrip('\n'))
            for i in range(n):
                lWords.append(fd.readline().rstrip('\n'))
            #print("All words:\n" + str(lWords), file = sys.stderr)
            
            grid = {}
            h, w = [int(i) for i in fd.readline().rstrip('\n').split()]
            for i in range(h):
                grid[i] = {}
                lLine = list(fd.readline().rstrip('\n'))
                for j in range(w):
                    grid[i][j] = lLine[j]
            #print("\nGrid:\n" + str(grid), file = sys.stderr)
            
            marked = [[False for r in range(h)] for c in range(w)]

            for wrd in lWords:
                searchWord(wrd, grid)

            secret = []
            for rMark in range(len(marked)):
                for cMark in range(len(marked[rMark])):
                    if not marked[rMark][cMark]:
                        secret.append(grid[rMark][cMark])

            print(''.join(secret))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
