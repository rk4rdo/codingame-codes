# Number of paths between 2 points

#### [Codingame URL](https://www.codingame.com/ide/puzzle/number-of-paths-between-2-points)
#### Python 3.7.3

## Description
Given a two dimensional array representing a map, find the total number
of paths between two opposite points (0, 0) and (N-1, M-1). You can only
move from left to right and from top to bottom.

Value 0 means that you are free to go on a cell, value 1 is a non
reachable cell.

## Input
- Line 1 : An int M for the number of rows.
- Line 2 : An int N for the number of cols.
- M next lines: A String representing the values of the cells of the
row: 0 for an empty cell or 1 for a wall

## Output
- Line 1 : An int representing the number of paths between the two
opposite points of the map

## Constraints
- 1 ≤ M ≤ 10
- 1 ≤ N ≤ 10

## Example
### Input
> 2\
2\
00\
00

### Output
> 2

## Execution example
```
python code039.py <file_path>
```

> **_<file_path>_** *Path to the input file*
