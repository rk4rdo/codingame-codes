# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:35:42 2018

@author: rvillareal
"""

import os
import sys
import math

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            candidates = {}
            nCandidates = int(fd.readline())
            for k in range(1, nCandidates + 1):
                candidates[k] = fd.readline().rstrip()
            votes = {}
            nVotes = int(fd.readline())
            for k in range(nVotes):
                votes[k] = [[int(q) for q in fd.readline().split()], 0]
            
            # First loop
            result = {k: 0 for k in range(1, nCandidates + 1)}
            for k in votes:
                lVote = votes[k][0]
                oVote = votes[k][1]
                result[lVote[oVote]] += 1
            
            allCandidates = list(candidates.keys())
            while allCandidates:
                # Search for candidate with min. number of votes
                minVotes = math.inf
                minCandidates = []
                for k in result:
                    if result[k] < minVotes:
                        minVotes = result[k]
                        minCandidates = [k]
                    elif result[k] == minVotes:
                        minCandidates.append(k)
                
                # Rmv cand. with min. num. of votes (first if more than one)
                rmvCandidate = min(minCandidates)
                allCandidates.remove(rmvCandidate)
                result.pop(rmvCandidate, None)
                # Show removed candidate
                print(candidates[rmvCandidate])
                # Check if remains at least 2 or more candidates
                if len(allCandidates) > 1:
                    # Re-calculate result
                    for k in votes:
                        lVote = votes[k][0]
                        oVote = votes[k][1]
                        if lVote[oVote] == rmvCandidate:
                            # Search next candidate voted
                            while (lVote[oVote] not in allCandidates) and\
                                    oVote < len(lVote):
                                votes[k][1] += 1
                                oVote = votes[k][1]
                            
                            if lVote[oVote] in allCandidates:
                                result[lVote[oVote]] += 1
                else:
                    # Show winner candidate
                    print("winner:" + candidates[allCandidates[0]])
                    break
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)