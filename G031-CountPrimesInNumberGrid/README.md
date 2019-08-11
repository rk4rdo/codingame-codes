# Count of Primes in a number grid

#### [Codingame URL](https://www.codingame.com/ide/puzzle/count-of-primes-in-a-number-grid)
#### Python 3.7.3
#### Libraries
- **more-itertools** **_-_** _Version: 6.0.0_

## Description
Given a grid of single digit numbers in R rows and C columns, count the
number of distinct primes that can be found using Across or Down reading
order. Partial use of the numbers in any direction is allowed, but
skipping digits is not.

Example in the grid below:
<pre>
2 3
1 7
</pre>

The primes that can found are : 2, 3, 7, 17, 23, 37.

So, the output would be 6. Note that 13 and 71 are not counted as they
are not a result of using the across or down reading order.

## Input
- Line 1: Two numbers R and C, separated by a single space
- Next R lines: Depicts a grid of single digit numbers, separated by a
single space

## Output
- One single number depicting the count of distinct primes found in the
grid. Do not count duplicates.

## Constraints
- 2<=R<=8
- 2<=C<=8

## Example
### Input
> 2 2\
2 3\
1 7

### Output
> 6

## Execution example
```
python code031.py <file_path>
```

> **_<file_path>_** *Path to the input file*
