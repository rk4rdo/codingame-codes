# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 18:20:35 2018

@author: rvillareal
"""

import os
import sys
import math

# Transform km/h to m/s
def kmH2mS(spd):
    return(spd * 1000 / 3600)

# Transform km/h to m/s
def mS2kmH(spd):
    return(spd * 3600 / 1000)

# Check if two numbers are nearly equal
def nearlyEqual(a, b, sigFig = 2):
    return (a == b or abs(b - a) < 1e-10)

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            maxSpd = int(fd.readline().rstrip())
            nTrfL = int(fd.readline().rstrip())
            trfL = {}
            for tL in range(nTrfL):
                dTL, tTL = [int(k) for k in fd.readline().rstrip().split()]
                trfL[dTL] = tTL

            # Get max. speed for green lights
            spd = 60
            for spd in range(maxSpd, 0, -1):
                # Transform km/h to m/s
                spd = kmH2mS(spd)
                # Boolean to indicate if the car pass all the traffic lights
                found = True
                # Check all traffic lights
                for tL in trfL:
                    # Calculate seconds to reach that point
                    tmp = tL / spd
                    # Check if in that time the traffic light is green or red
                    dTmp = tmp / trfL[tL]
                    cTmp = math.ceil(dTmp)
                    nTmp = cTmp if nearlyEqual(dTmp, cTmp) else int(dTmp)
                    
                    if nTmp % 2 != 0:
                        found = False
                        break
                
                if found:
                    break
            
            print(round(mS2kmH(spd)))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
