# Rugby score

#### [Codingame URL](https://www.codingame.com/ide/puzzle/rugby-score)
#### Python 3.7.3
#### Libraries
- **numpy** **_-_** _Version: 1.16.2_

## Description
Given a rugby score, your program must compute the different scoring
combinations that lead to that particular score.

As a reminder:
- A try is worth 5 points
- After a try, a transformation kick is played and is worth 2 extra
points if successful
- Penalty kicks and drops are worth 3 points

## Input
- Line 1: the score

## Output
- N lines: number of tries, number of transformations, number of
penalties / drops, separated by spaces

The combinations must be ordered by increasing order of tries, then
transformations, then penalties/drops

## Constraints
No impossible scores are given, there is always at least one valid
combination.

## Example
### Input
> 12

### Output
> 0 0 4\
2 1 0

## Execution example
```
python code016.py <file_path>
```

> **_<file_path>_** *Path to the input file*
