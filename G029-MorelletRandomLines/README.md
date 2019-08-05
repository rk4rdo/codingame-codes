# Morellet's random lines

#### [Codingame URL](https://www.codingame.com/ide/puzzle/morellets-random-lines)

## Description
You are a modern artist and you like drawing random lines on a sheet of
paper like François Morellet.

These lines draw a somewhat strange chess board that you fill with only
two colours.

You are given the lines and the coordinates of two point A and B and you
have to tell if the points have the same colour or not or if one of them
is on one line.

You will be given the coefficients of each line (Cartesian style,
ie ax+by+c=0, a, b and c given).

Count each line once because sometimes, some lines might have more than
one equation in the list.

For example, 2x+4y+6=0 is the same line than x+2y+3=0.
a and b can’t be null at the same time.

## Input
- Line 1: xA yA xB yB
- Line 2: n, the number of straight lines
- Next n lines: a b c for each line

## Output
- If at least A or B is on one line, print ON A LINE
- If not, print YES if A and B have the same colour, else NO

## Example
### Input
1 1 0 0\
1\
1 2 3

### Output
> YES

## Execution example
```
python code029.py <file_path>
```

> **_<file_path>_** *Path to the input file*
