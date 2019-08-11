# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:10:37 2018

@author: rvillareal
"""

import os
import sys
from datetime import datetime
from dateutil import relativedelta

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            
            b = datetime.strptime(fd.readline().rstrip(), '%d.%m.%Y')
            e = datetime.strptime(fd.readline().rstrip(), '%d.%m.%Y')
            
            relativedelta.relativedelta(e, b)
            
            d = (e - b).days
            y = relativedelta.relativedelta(e, b).years
            m = relativedelta.relativedelta(e, b).months
            
            labY = (str(y) + " year" + ("s" if y > 1 else "")) if y > 0 else ""
            labM = (str(m) + " month" + ("s" if m > 1 else "")) if m > 0 else ""
            labD = "total " + str(d) + " day" + ("s" if d > 1 or d == 0 else "")
            
            msg = ""
            for lab in [lb for lb in [labY, labM, labD] if lb != ""]:
                msg += (", " if msg != "" else "") + lab
            
            print(msg)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
