# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:49:52 2018

@author: rvillareal
"""

import os
import sys
import itertools as it

def primeFactors(n):
    for i in it.chain([2], it.count(3, 2)):
        if n <= 1:
            break
        while n % i == 0:
            n //= i
            yield i

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            columns = {}
            nR, nC = [int(k) for k in fd.readline().rstrip().split()]
            
            allPrimes = set()
            for r in range(nR):
                row = [int(k) for k in fd.readline().rstrip('\n').split()]
                for c in range(nC):
                    if c not in columns:
                        columns[c] = [row[c]]
                    else:
                        columns[c].append(row[c])
                # Check 1-solo elements
                for c in range(nC):
                    if len(list(primeFactors(row[c]))) == 1:
                        allPrimes.add(row[c])
                # Check row elements (right to left)
                for beg in range(nC - 1):
                    for end in range(beg + 1, nC):
#                        print("Checking " + str(row[beg:(end + 1)]))
                        allnums =  [str(k) for k in row[beg:(end + 1)]]
                        num = int("".join(allnums))
                        if len(list(primeFactors(num))) == 1:
                            allPrimes.add(num)
            
            # Check column elements (up to down)
            for col in range(nC):
                for beg in range(nR - 1):
                    for end in range(beg + 1, nR):
#                        print("Checking " + str(columns[col][beg:(end + 1)]))
                        allnums = [str(k) for k in columns[col][beg:(end + 1)]]
                        num = int("".join(allnums))
                        if len(list(primeFactors(num))) == 1:
                            allPrimes.add(num)
            
            print(len(allPrimes))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
