# Disordered First Contact

#### [Codingame URL](https://www.codingame.com/ide/puzzle/disordered-first-contact)
#### Python 3.7.3

## Description
Finally, we have received the first messages from aliens!

Unfortunately we cannot understand them because they have a very unique
way of speaking.

Here is how aliens encode their messages:
- At each step of the encoding, they remove a bigger part from the
beginning of the original message, starting from 1 character only.
First, they take the first character, then 2 characters, then 3, etc...
- Starting from an empty result string, they add each part taken from
the original message alternatively at the end and at the beginning of
the result string. They add the first part at the end, the second part
at the beginning, the third part at the end, etc...

### Example
abcdefghi becomes ghibcadef

1. Take "a" from abcdefghi, add it at the end of an empty string
	> a
2. Take "bc" from bcdefghi, add it at the beginning
	> bca
3. Take "def" from defghi, add it at the end
	> bcadef
4. Take the remaining characters "ghi" and add it at the beginning
	> ghibcadef

Some messages have been transformed using the above method more than
once.

Your job here is to decode or encode the messages to discuss with
aliens.

## Input
- Line 1: An integer N indicating the number of times the message was
transformed. If N is positive you have to decode i.e. retrieve the
original message. If N is negative you have to encode i.e. transform
the message.
- Line 2: A string message to be decoded or encoded.

## Output
- One line: The original message (if N is positive) or the transformed
message (if N is negative).

## Constraints
- -10 ≤ N ≤ 10
- 0 < message length < 1024

## Example
### Input
> 1\
ghibcadef

### Output
> abcdefghi

## Execution example
```
python code008.py <file_path>
```

> **_<file_path>_** *Path to the input file*
