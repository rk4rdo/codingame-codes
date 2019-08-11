
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 17:55:57 2019

@author: zokk
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:39:02 2018

@author: rvillareal
"""

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:

            n = int(fd.readline().rstrip())
            msg = fd.readline().rstrip('\n')
            
            k = 1
            tot = 0
            while tot < len(msg):
                tot += k
                k += 1
            k -= 1
            tot -= k
            remain = len(msg) - tot
                
            if n > 0:
#                print("Decoding", file = sys.stderr)
                for tN in range(n):
                    dec = ""
                    
                    front = True if k % 2 == 0 else False
                    positions = list([remain])
                    positions.extend(list(range(k - 1, 0, -1)))
                    for h in positions:
                        if front:
                            dec += msg[:h][::-1]
                            msg = msg[h:]
                        else:
                            dec += msg[-h:][::-1]
                            msg = msg[:-h]            
                        front = False if front else True
                    
                    msg = dec[::-1]
#                    print("Decode " + str(tN + 1) + ": " + msg,
#                          file = sys.stderr)
            elif n < 0:
#                print("Encoding", file = sys.stderr)
                for tN in range(abs(n)):
                    enc = ""
                    
                    front = True
                    for h in range(1, k):
                        if front:
                            enc += msg[:h]
                        else:
                            enc = msg[:h] + enc
                        msg = msg[h:]
                        front = False if front else True
                    
                    msg = enc + msg[:remain] if front else msg[:remain] + enc
#                    print("Encode " + str(tN + 1) + ": " + msg,
#                          file = sys.stderr)
            
            print(msg)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
