# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:04:00 2018

@author: rvillareal
"""

import os
import sys

def reconstructPath(cameFrom, curr):
    path = [curr]
    while curr in cameFrom.keys():
        curr = cameFrom[curr]
        path.append(curr)
    return(path[::-1])

def AStar(s, g):
    # Set of nodes already evaluated
    passNodes = []
    passFVals = []
    
    # Set of neighbours from current node. Initially contains start node.
    openNodes = [s]
    
    # Actual cost from start to each node, starts with 0 for start node
    # Map with keys -> iden. nodes and values -> G-value
    nodGVal = {s: 0}
    
    # Map with keys -> iden. nodes and values -> iden. came from node
    cameFrom = {}
    
    # Var to save final path
    finalPath = None
    
    # List with nodes ordered by opening time
    orderNodes = []
    
    while bool(openNodes):
        curr = None
        # Map with keys -> F-value and values -> iden. nodes
        nodFVal = {}
        
        for node in openNodes:
            fVal = nodHVal[node] + nodGVal[node]
            if fVal not in nodFVal:
                nodFVal[fVal] = [node]
            else:
                nodFVal[fVal].append(node)
        curr = min(nodFVal[min(nodFVal.keys())])
        
        openNodes.remove(curr)
        passNodes.append(curr)
        passFVals.append(min(nodFVal.keys()))
        orderNodes.append(curr)
        if curr == g:
            finalPath = reconstructPath(cameFrom, curr)
            break
        
        neighbours = [k for k in nodEdges[curr].keys() if k not in passNodes]
        for neigh in neighbours:
            neighGVal = nodGVal[curr] + nodEdges[curr][neigh]
            
            if neigh not in openNodes:
                openNodes.append(neigh)
            else:
                if neigh in nodGVal.keys():
                    # Bad path
                    if neighGVal >= nodGVal[neigh]:
                        continue
            
            cameFrom[neigh] = curr
            nodGVal[neigh] = neighGVal
    
    return finalPath, passFVals, orderNodes

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as fd:
            n, e, s, g = [int(i) for i in fd.readline().split()]
            
            # Estimated distances to the goal (heuristics) for each node
            # Map with keys -> iden. nodes and values -> H-value
            k = 0
            nodHVal = {}
            for i in fd.readline().split():
                nodHVal[k] = int(i)
                k += 1
            
            # Map with all nodes and their connections with associated costs
            nodEdges = {}
            for i in range(e):
                x, y, c = [int(j) for j in fd.readline().split()]
                if x not in nodEdges:
                    nodEdges[x] = {}
                if y not in nodEdges:
                    nodEdges[y] = {}
                nodEdges[x][y] = nodEdges[y][x] = c
            
            finalPath, passFVals, orderNodes = AStar(s, g)
            
            for k in range(len(orderNodes)):
                print(" ".join([str(orderNodes[k]), str(passFVals[k])]))
    else:
        print("[ERROR] Process needs file with data")
        sys.exit(1)
else:
    print("[ERROR] Process needs file with data")
    sys.exit(1)
