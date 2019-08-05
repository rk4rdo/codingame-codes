# -*- coding: utf-8 -*-
"""
@author: rvillareal
"""
# Example 1 [Solution => L U]
line1 = "z"
line2 = "D"
line3 = "L"

# Example 2 [Solution => U R]
line1 = "y z'"
line2 = "B"
line3 = "D"

# Example 3 [Solution => B L]
line1 = "x y x' z y'"
line2 = "L"
line3 = "B"

# Example 4 [Solution => F D]
line1 = "x y x y x y"
line2 = "F"
line3 = "D"

# Example 5 [Solution => F D]
line1 = "x y z x z y y x z y z x z x y z y x"
line2 = "L"
line3 = "F"

# Example 5 [Solution => L U]
line1 = "x x x y y y z z z"
line2 = "B"
line3 = "U"

#%%

rots = [k for k in line1.split()]
srchFc = [line2]
srchFc.append(line3)

wiseFaces = {'x': ['F', 'U', 'B', 'D'],
             'y': ['F', 'L', 'B', 'R'],
             'z': ['U', 'R', 'D', 'L']}
for rot in rots:
    counter = True if len(rot) > 1 else False
    axis = rot[0]
    for iSrch in range(len(srchFc)):
        if srchFc[iSrch] in wiseFaces[axis]:
            pos = wiseFaces[axis].index(srchFc[iSrch])
            if not counter:
                pos = pos + 1 if pos + 1 < len(wiseFaces[axis]) else 0
            else:
                pos = pos -1 if pos - 1 >= 0 else len(wiseFaces[axis]) - 1
            srchFc[iSrch] = wiseFaces[axis][pos]

for fc in srchFc:
    print(fc)
