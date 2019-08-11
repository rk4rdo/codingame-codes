# Text formatting

#### [Codingame URL](https://www.codingame.com/ide/puzzle/text-formatting)

## Description
Format a text file using the following rules:

- Only a single space between words (remove excessive spaces).
- No spaces before punctuation marks.
- One space after each punctuation mark in front of a letter.
- Use only lowercase letters, except for the beginning of the sentence
(after a dot).
- Remove repeated punctuation marks.

A punctuation mark is a character other than a space, a letter or a
digit.

Example
- Input: "when a father gives to his son,,, Both laugh; When a son gives
to his father, , , Both cry...shakespeare"
- Output: "When a father gives to his son, both laugh; when a son gives to
his father, both cry. Shakespeare"

## Input
- A line of text.

## Output
- A line containing the Formatted text.

## Constraints
- The length of the input string is less than 1000.

## Example
### Input
> one,two,three.

### Output
> One, two, three.

## Execution example
```
python code028.py <file_path>
```

> **_<file_path>_** *Path to the input file*
