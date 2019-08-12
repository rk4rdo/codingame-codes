# Factorial vs Exponential

#### [Codingame URL](https://www.codingame.com/ide/puzzle/factorial-vs-exponential)
#### Python 3.7.3
#### Libraries
- **decimal** **_-_** _Version: 1.70_

## Description
For each of the given numbers A, find the smallest integer N, such that:
- A^N < N!
- N! = 1 * 2 * ... * N

The numbers given can have up to 2 digits after decimal point.

## Input
- Line 1: An integer K for the number of inputs.
- Line 2: K space separated numbers (can have a fractional part, e.g.
1.5) => A_1, A_2, ... , A_K

## Output
- Line 1: K space separated integers => N_1, N_2, ... , N_K

## Constraints
- 1 ≤ K ≤ 100
- 1 < A_i < 10000

## Example
### Input
> 2\
2 3

### Output
> 4 7

## Execution example
```
python code023.py <file_path>
```

> **_<file_path>_** *Path to the input file*
