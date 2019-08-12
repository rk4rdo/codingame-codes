# Expand the polynomial

#### [Codingame URL](https://www.codingame.com/ide/puzzle/expand-the-polynomial)
#### Python 3.7.3
#### Libraries
- **numpy** **_-_** _Version: 1.16.2_

## Description
You are given a polynomial that is partially or fully factorized and you
have to write a code that fully expands it.

For example, if you are given
<pre>(x-1)*(x+2)=x²+x-2</pre>
Its coefficients that are 1 1 -2 and you have to write x^2+x-2.

## Input
- A partially or not factorized polynomial.

## Output
- The expanded polynomial written in the standard way:
	- x^1 is written x
	- 1x^3 is written x^3
	- 0x^2 and x^0 are not written

## Constraints
- All the coefficients are integers (positive, null or negative).
- All coefficients are in decreasing order: (x^3 then x^2 then x^1 then
x^0)

## Example
### Input
<pre>(x-1)*(x+2)</pre>

### Output
<pre>x^2+x-2</pre>

## Execution example
```
python code034.py <file_path>
```

> **_<file_path>_** *Path to the input file*
