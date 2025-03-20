# Sparse Arrays

`https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true`

## Problem Description

There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

## Function Description

Complete the function `matchingStrings` which returns an integer array of the results.

## Input Format

- The first line contains an integer `n`, the size of the input strings array.
- Each of the next `n` lines contains a string `strings[i]`.
- The next line contains an integer `q`, the size of the query strings array.
- Each of the next `q` lines contains a string `queries[i]`.

## Output Format

Return an array of integers where each element is the count of occurrences of the corresponding query string.

## Example

Input:
```
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
```

Output:
```
2
1
0
```

Explanation:
- 'aba' appears twice in the input strings
- 'xzxb' appears once
- 'ab' does not appear at all
