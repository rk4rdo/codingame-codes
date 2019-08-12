# Cryptarithm

#### [Codingame URL](https://www.codingame.com/ide/puzzle/cryptarithm)
#### Python 3.7.3

## Description
Given an initial list of actions to do, and a partial chronological
order, output the actions in the right order.

## Input
- Line 1: An integer N for the number of actions.
- Next N lines: A unique action to perform.
- Next line: An integer nbOrders for the numbers of precedence.
- Next nbOrders lines: a line in the form a1 precedence a2, where
precedence is either before if action a1 must be done before action a2,
or after if action a1 must be done after action a2.

## Output
- One action per line in chronological order. If multiple actions can be
done at the same time, choose the one that appears first in the intitial
order.

## Constraints
- 1 < N < 10

## Example
### Input
<pre>
3
Close
Open
Pour
2
Open before Pour
Close after Pour
</pre>

### Output
<pre>
Open
Pour
Close
</pre>

## Execution example
```
python code026.py <file_path>
```

> **_<file_path>_** *Path to the input file*
