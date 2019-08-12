# Hidden word

#### [Codingame URL](https://www.codingame.com/ide/puzzle/hidden-word)
#### Python 3.7.3

## Description
You are given a grid of letters and a list of words.

Strike the words in the grid. They can be written horizontally,
vertically or diagonally, possibly reversed (in any direction) but
always in a straight line. Each word is found only once in the grid,
although they may overlap.

A few letters will remain unstruck. Write them down, from left to right,
top to bottom, and find the secret word.

## Input
- Line 1: The number n of words
- Next n lines: A word
- Next line: The heigth and width of the grid
- Next h lines: A string

## Output
- Print the word

## Constraints
- The strings are not too long, i.e. their length is below 40.
- The length of the lines of the grid is the same.
- You can assume that every word and string contains only the 26 letters
of the alphabet in capitals.

## Example
### Input
<pre>
2
BAC
BOB
3 3
BAC
BOB
RED
</pre>

### Output
<pre>
RED
</pre>

## Execution example
```
python code001.py <file_path>
```

> **_<file_path>_** *Path to the input file*
