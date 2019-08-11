# How time flies

#### [Codingame URL](https://www.codingame.com/ide/puzzle/how-time-flies)
#### Python 3.7.3
#### Libraries
- python-dateutil _Version: 2.8.0_
- DateTime _Version: 4.3_

## Description
Your program must print formatted string with the number of full years
and full months (if there are any greater than 0) and the total number
of days between BEGIN and END dates in dd.mm.yyyy format.

### Example 1:
#### Input:
> 01.01.2000\
01.01.2016

#### Output:
> 16 years, total 5844 days

### Example 2:
#### Input:
> 15.12.2014\
14.02.2016

#### Output:
> 1 year, 1 month, total 426 days

### Example 3:
#### Input:
> 01.01.2016\
18.08.2016

#### Output:
> 7 months, total 230 days

## Input
- Line 1: A date BEGIN in dd.mm.yyyy format.
- Line 2: A date END in dd.mm.yyyy format.

## Output
- Line 1: Formatted string presenting date difference as "YY year[s], MM month[s], total NN days"

## Constraints
- BEGIN ≤ END

## Example
### Input
> 01.01.2000\
01.01.2016

### Output
> 16 years, total 5844 days

## Execution example
```
python code025.py <file_path>
```

> **_<file_path>_** *Path to the input file*
