# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:55:21 2018

@author: rvillareal
"""

import os
import sys
import operator

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            orig = []
            actions = {}
            n = int(fd.readline().rstrip('\n'))
            for a in range(n):
                act = fd.readline().rstrip('\n')
                orig.append(act)
                actions[act] = a
            
            rules = {}
            constraints = []
            nC = int(fd.readline().rstrip('\n'))
            for c in range(nC):
                x, s, y = [k for k in fd.readline().rstrip('\n').split()]
                constraints.append((x, s, y))
                if x not in rules:
                    rules[x] = [y]
                else:
                    rules[x].append(y)
                if y not in rules:
                    rules[y] = [x]
                else:
                    rules[y].append(x)
            
            sol = False
            while not sol:
                sol = True
                
                for c in constraints:
                    x, s, y = c
                    if s == "before" and actions[x] >= actions[y]:
                        sol = False
                        actions[x], actions[y] = actions[y], actions[x]
                        break
                    elif s == "after" and actions[x] <= actions[y]:
                        sol = False
                        actions[x], actions[y] = actions[y], actions[x]
                        break
            
            pActions = sorted(actions.items(), key = operator.itemgetter(1))
            pActions = [k[0] for k in pActions]
            h = 0
            fActions = []
            while h != len(pActions):
                lSub = [pActions[h]]
                for q in range(h + 1, len(pActions)):
                    if pActions[q] not in rules[pActions[h]]:
                        lSub.append(pActions[q])
                    else:
                        break
                
                if len(lSub) > 1:
                    lSub = [k for k in orig if k in lSub]
                    h += len(lSub)
                else:
                    h += 1
                
                fActions.extend(lSub)
            
            for a in fActions:
                print(a)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
