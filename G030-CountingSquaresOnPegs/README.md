# Counting  Squares on Pegs

#### [Codingame URL](https://www.codingame.com/ide/puzzle/counting-squares-on-pegs)
#### Python 3.7.3

## Description
A farmer wishes to delimit a square plot of land in his field by setting
up a square fence. To this end, he needs to place 4 pegs at the 4
(distinct) corner positions beforehand. The pegs can only be placed at
some given positions where the ground has the appropriate softness (not
too hard so that it is possible to hammer the pegs deep enough, but not
too soft so that the pegs support the fence without falling).

Given the possible integer positions for the pegs, in how many ways can
the farmer pick 4 distinct positions to form a square?

Note that we do not require the squares to be axis-aligned.

## Input
- Line 1: An integer N denoting the number of valid positions for pegs
in the field.
- Next N lines: Two space-separated integers X and Y denoting some
acceptable coordinates for a peg in the field (given in lexicographical
order and without duplicates).

## Output
- A single integer denoting the number of squares that can be formed
using the given vertices (pegs).

## Constraints
- 4≤N≤2000
- 0≤X≤N-1
- 0≤Y≤N-1

## Example
### Input
> 5\
0 0\
0 2\
1 0\
2 0\
2 2

### Output
> 1

## Execution example
```
python code030.py <file_path>
```

> **_<file_path>_** *Path to the input file*
