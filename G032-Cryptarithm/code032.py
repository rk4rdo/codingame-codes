# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 13:41:12 2018

@author: rvillareal
"""

import os
import sys

def getEncrytation(letDict, words, res):
    avail = [k for k in letDict if letDict[k][0] < 0]
    if avail:
        nL = avail[0]
        usedNums = [k[0] for k in letDict.values() if k[0] >= 0]
        nums = [k for k in range(1 if letDict[nL][1] else 0, 10)
                if k not in usedNums]
        for n in nums:
            nLetters = letDict.copy()
            nLetters[nL] = (n, letDict[nL][1])
            if getEncrytation(nLetters, words, res):
                return True
    else:
        lNums = []
        for wrd in words:
            num = int("".join([str(letDict[k][0]) for k in wrd]))
            lNums.append(num)
        posRes = int("".join([str(letDict[k][0]) for k in res]))
        if sum(lNums) == posRes:
            for let in sorted(letDict.keys()):
                print(let + " " + str(letDict[let][0]))
            return True
        else:
            return False

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            words = []
            letters = {}
            n = int(fd.readline().rstrip('\n'))
            for i in range(n):
                w = fd.readline().rstrip('\n')
                nLetters = list(set([k for k in list(w) if k not in letters]))
                for nL in nLetters:
                    letters[nL] = (-1, False)
                letters[w[0]] = (-1, True)
                words.append(w)
            
            res = fd.readline().rstrip('\n')
            nL = list(set([k for k in list(res) if k not in letters]))
            for nL in nL:
                letters[nL] = (-1, False)
            letters[res[0]] = (-1, True)
            
            getEncrytation(letters, words, res)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
