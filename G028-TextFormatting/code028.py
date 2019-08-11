# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 13:07:51 2018

@author: rvillareal
"""

import os
import re
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            # Read file
            msg = fd.read().rstrip()
            
            # Only one single space between words (remove excessive spaces)
            msg = re.sub("(\s)+", r"\1", msg)
            # No spaces before punctuation marks
            msg = re.sub("\s+([^\w\s])", r"\1", msg)
            # One space after each punctuation mark in front of a letter
            msg = re.sub("([^\w\s])(\w)", r"\1 \2", msg)
            # Remove repeated punctuation marks
            msg = re.sub("([^\w\s])+", r"\1", msg)
            # Use only lowercase letters, except for the beginning of the
            # sentence (after a dot)
            msg = str.lower(msg)
            print(". ".join([str.capitalize(k) for k in msg.split(". ")]))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)