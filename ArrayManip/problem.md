# Array Manipulation

## Problem Statement
Given an array of `n` zeros (1-indexed) and a list of operations, perform each operation by adding a value to all elements between two given indices (inclusive). After performing all operations, find and return the maximum value in the array.

### Input Format
- First line: two integers `n` and `m` where:
  - `n` is the size of the array (1 to 10⁷)
  - `m` is the number of operations (1 to 2×10⁵)
- Next `m` lines: three integers `a`, `b`, and `k` where:
  - `a` is the starting index
  - `b` is the ending index
  - `k` is the value to add (0 to 10⁹)

### Output Format
Return a single integer denoting the maximum value in the final array.

### Example 1
**Input:**
```
5 3
1 2 100
2 5 100
3 4 100
```

**Initial array:** [0, 0, 0, 0, 0]

**After first operation:** [100, 100, 0, 0, 0]

**After second operation:** [100, 200, 100, 100, 100]

**After third operation:** [100, 200, 200, 200, 100]

**Output:** 
```
200
```

### Constraints
- 1 ≤ n ≤ 10⁷
- 1 ≤ m ≤ 2×10⁵
- 1 ≤ a ≤ b ≤ n
- 0 ≤ k ≤ 10⁹

### Notes
- The array is 1-indexed
- Each operation is inclusive of both start and end indices
- Time complexity should be considered due to large constraints
