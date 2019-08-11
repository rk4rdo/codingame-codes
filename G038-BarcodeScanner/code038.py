# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 13:27:12 2019

@author: rvillarg
"""

class Ean13coder:
    
    # Singleton instance
    instance = None
    
    class __Ean13coder:
        
        # Verification constants
        LENC = 7
        LENP = 42
        CGUARD = '01010'
        LRGUARD = '101'
        LENBAR = 95
        
        # Constant messages
        ERRMSG = "INVALID SCAN"
        
        # Digits LGR-codification
        __enc = {0: {'L': '0001101', 'G': '0100111', 'R': '1110010'},
                 1: {'L': '0011001', 'G': '0110011', 'R': '1100110'},
                 2: {'L': '0010011', 'G': '0011011', 'R': '1101100'},
                 3: {'L': '0111101', 'G': '0100001', 'R': '1000010'},
                 4: {'L': '0100011', 'G': '0011101', 'R': '1011100'},
                 5: {'L': '0110001', 'G': '0111001', 'R': '1001110'},
                 6: {'L': '0101111', 'G': '0000101', 'R': '1010000'},
                 7: {'L': '0111011', 'G': '0010001', 'R': '1000100'},
                 8: {'L': '0110111', 'G': '0001001', 'R': '1001000'},
                 9: {'L': '0001011', 'G': '0010111', 'R': '1110100'}}
        
        # First digit EAN-13
        __ean13 = {'LLLLLL': 0, 'LLGLGG': 1, 'LLGGLG': 2, 'LLGGGL': 3,
                   'LGLLGG': 4, 'LGGLLG': 5, 'LGGGLL': 6, 'LGLGLG': 7,
                   'LGLGGL': 8, 'LGGLGL': 9}
        
        # Default constructor
        def __init__(self):
            pass
        
        def __decodeLeft(self, lbar):
            # Left part
            valid = True
            ldigits = []
            ean13mode = []
            lcodes = [lbar[k:k + self.LENC]
                        for k in range(0, len(lbar), self.LENC)]
            for lc in lcodes:
                nMod = [(k, l) for k in self.__enc
                            for l in self.__enc[k] if self.__enc[k][l] == lc]
                if len(nMod) == 1:
                    n, m = nMod[0]
                    ldigits.append(n)
                    ean13mode.append(m)
                else:
                    valid = False
                    break
            
            return valid, ldigits, ean13mode
        
        def __decodeRight(self, rbar):
            # Right part
            valid = True
            rdigits = []
            rcodes = [rbar[k:k + self.LENC]
                        for k in range(0, len(rbar), self.LENC)]
            for rc in rcodes:
                n = [k for k in self.__enc if self.__enc[k]['R'] == rc]
                if len(n) == 1:
                    rdigits.extend(n)
                else:
                    valid = False
                    break
            
            return valid, rdigits
        
        def __verifyChecksum(self, barcode):
            neven = sum([barcode[k] for k in range(0, len(barcode), 2)])
            nodd = sum([barcode[k] * 3 for k in range(1, len(barcode), 2)])
            return True if ((neven + nodd) % 10) == 0 else False
        
        # Decode bar
        def decode(self, bar):
            
            # Bar length & extreme codes verification
            validLen = len(bar) == self.LENBAR
            validLft = bar.startswith(self.LRGUARD)
            validRht = bar.endswith(self.LRGUARD)
            if validLen and validLft and validRht:
                bar = bar[len(self.LRGUARD):-len(self.LRGUARD)]
                lbar = bar[:self.LENP]
                rbar = bar[-self.LENP:]
                bar = bar[len(lbar):-len(rbar)]
                # Bar center code verification
                validCnt = bar == self.CGUARD
                if validCnt:
                    rdigits = []
                    # Try barcode in right position
                    vl, ldigits, ean13mode = self.__decodeLeft(lbar)
                    if vl:
                        vr, rdigits = self.__decodeRight(rbar)
                    
                    # Try barcode in reverse position
                    if not vl or not vr:
                        vl, ldigits, ean13mode = self.__decodeLeft(rbar[::-1])
                        if vl:
                            vr, rdigits = self.__decodeRight(lbar[::-1])
                    
                    if vl and vr:
                        # EAN-13 First value
                        edigit = self.__ean13["".join(ean13mode)]
                        barcode = [k for k in [edigit] + ldigits + rdigits]
                        validChecksum = self.__verifyChecksum(barcode)
                        if validChecksum:
                            return (True, "".join([str(k) for k in barcode]))
                        else:
                            return (False, self.ERRMSG)
                    else:
                        return (False, self.ERRMSG)
                else:
                    return (False, self.ERRMSG)
            else:
                return (False, self.ERRMSG)

        def __str__(self):
            return repr(self)
    
    def __new__(cls):
        if not Ean13coder.instance:
            Ean13coder.instance = Ean13coder.__Ean13coder()
        return Ean13coder.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)

import os
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            bar = fd.readline().rstrip('\n')
            
            decoder = Ean13coder()
            valid, decodeBar = decoder.decode(bar)
            print(decodeBar)
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
