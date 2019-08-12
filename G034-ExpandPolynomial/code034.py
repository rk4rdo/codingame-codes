# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:51:54 2019

@author: rvillareal
"""
# Example 1 [Solution: x^2+x-2]
line1 = "(x-1)*(x+2)"

# Example 2 [Solution: x^2-4x+4]
line1 = "(x-2)^2"

# Example 3 [Solution: x^2-4]
line1 = "(x-2)(x+2)"

# Example 4 [Solution: 16x^5-24x^4+37x^3-16x^2+8x-1]
line1 = "(4x^3-5x^2+7x-1)(4x^2-x+1)"

# Example 5 [Solution: x^4-1]
line1 = "(x-1)(x+1)(x^2+1)"

# Example 6 [Solution: 2x^4-x^3-8x^2+x+6]
line1 = "(2x^2+x-3)(x^2-x-2)"

#%%

import re
import os
import sys
import numpy.polynomial.polynomial as npp

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            p = fd.readline().rstrip('\n')
            
            k = 0
            comps = re.findall("\((.*?)\)", p)
            opers = re.findall("\)(.*?)(?:\(|$)", p)
            opers = opers[:-1] if opers[-1] == "" else opers
            
            cf = re.findall("((?:\+|-|)\d*)(?:x|$)", comps[k])[:-1]
            cf = [1 if q in ('', "+") else -1 if q == "-" else int(q)
                  for q in cf]
            gr = re.split("\+|-", comps[k])
            gr = [re.search("\d*$", g).group() if "x" in g else "0"
                  for g in gr]
            gr = [int(g) if g != "" else 1 for g in gr]
            fCoef = [cf.pop() if g in gr else 0 for g in range(max(gr) + 1)]
            pol = npp.Polynomial(coef = fCoef)
            k += 1
            for op in opers:
                if op == "*" or op == "":
                    cf = re.findall("((?:\+|-|)\d*)(?:x|$)", comps[k])[:-1]
                    cf = [1 if q in ('', "+") else -1 if q == "-" else int(q)
                          for q in cf]
                    gr = re.split("\+|-", comps[k])
                    gr = [re.search("\d*$", g).group() if "x" in g else "0"
                          for g in gr]
                    gr = [int(g) if g != "" else 1 for g in gr]
                    fCoef = [cf.pop() if g in gr else 0
                             for g in range(max(gr) + 1)]
                    c = npp.Polynomial(coef = fCoef)
                    k += 1
                    pol = npp.polymul(pol, c).any()
                elif op.startswith("^"):
                    g = int(op[1:])
                    pol = npp.polypow(pol, g).any()
            
            res = ""
            g = pol.degree()
            for i in [int(q) for q in pol.coef[::-1]]:
                if i != 0:
                    if g > 0:
                        a = ""
                        if g != pol.degree():
                            a += "+" if i > 0 else ""
                        a += "" if i == 1 else "-" if i == -1 else str(i)
                        b = a + "x" + ("" if g == 1 else "^" + str(g))
                        res += b
                    else:
                        res += str(i) if i < 0 else "+" + str(i)
                g -= 1
            
            print(res)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
