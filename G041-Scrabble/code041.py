#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 20:46:29 2019

@author: zokk
"""

import os
import sys

weights = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
           'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3,
           'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
           'y': 4, 'z': 10}

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            n = int(fd.readline().rstrip('\n'))
            profit = {}
            
            for w in range(n):
                word = fd.readline().rstrip('\n')
                profit[word] = sum([weights[l] for l in word])
            
            letters = fd.readline().rstrip('\n')
            dLetters = {}
            for w in letters:
                dLetters[w] = 1 if w not in dLetters else dLetters[w] + 1
            
            maxSc = 0
            maxWord = ""
            for w in profit:
                if profit[w] > maxSc:
                    dAux = dLetters.copy()
            
                    valid = True
                    for l in w:
                        if l in dAux and dAux[l] > 0:
                            dAux[l] -= 1
                        else:
                            valid = False
                            break
                    
                    if valid:
                        maxSc = profit[w]
                        maxWord = w
            
            print(maxWord)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
