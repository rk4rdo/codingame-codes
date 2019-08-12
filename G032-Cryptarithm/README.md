# Cryptarithm

#### [Codingame URL](https://www.codingame.com/ide/puzzle/cryptarithm)
#### Python 3.7.3

## Description
A cryptarithm is an equation where all digits have been replaced with a
letter, e.g. AA + BB = CC (this one may have several solutions), with:
- A = 1, B = 2 and C = 3
- A = 2, B = 3 and C = 5
- etc...

Your program must read the description of a cryptarithm and output the
solution to it.

In this puzzle:
- The supplied cryptarithms are all carried out as an addition
- They always have one single solution
- Each letter is assigned to a unique digit between 0 and 9 (i.e. two
different letters cannot be assigned to the same digit)
- The initial letter of a word can never be assigned to 0

## Input
- Line 1: N, the number of words to add up.
- N next lines: a string word containing a word to add up.
- Next line: a string total containing a word representing the sum of
all previous words.

## Output
- X lines: a letter and the digit assigned to it, separated by a space.
X is the number of distinct letters in the cryptarithm. The letters must
be given in alphabetical order.

## Constraints
- 2 ≤ N ≤ 5

## Example
### Input
<pre>
2
COCA
COLA
OASIS
</pre>

### Output
<pre>
A 6
C 8
I 9
L 0
O 1
S 2
</pre>

## Execution example
```
python code032.py <file_path>
```

> **_<file_path>_** *Path to the input file*
