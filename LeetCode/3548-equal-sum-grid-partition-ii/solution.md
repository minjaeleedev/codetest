# Approach: Rotation Matrix + Hash Table + Enumeration of the Upper Matrix Sum

## Intuition

This problem is an enhanced version of Equal Sum Grid Partition I, with additional constraints: at most one cell can be deleted, and the remaining part must remain connected after deletion.

When deletion is allowed, we need to consider both the choice of the split line and which side of the split to delete from. 
To simplify the reasoning, we assume that we only consider horizontal split lines and delete elements from the upper part of the grid.

By rotating the matrix three times by 90∘ and applying the same logic each time, we can cover all four possible orientations of the split line and deletion direction.

Next, we determine the condition for a valid partition:

1. Let the sum of the upper part of the current grid be sum, and the total sum of the grid be total. Then the sum of the lower part is total−sum.

2. Suppose we remove an element x. To make both parts equal, we must have
$sum−x=total−sum$, which simplifies to $x=2⋅sum−total$.

3. Therefore, after processing each row, we only need to check whether there exists an element grid[i][j] such that grid[i][j]=2⋅sum−total.

We use a set to store elements that have appeared so far, allowing efficient lookup.
We can pre-insert 0 into the set so that the "no deletion" case is handled naturally within the same logic.

Special cases:

1. First row handling:
    While processing the first row, only the first and last elements can be removed. After computing the sum of the first row, we check whether grid[0][0], grid[0][n−1], or 0 satisfies the condition.

2. Single-column grid:
    If the grid has only one column, the only removable elements are from the first or current row. After processing row i, we check whether grid[0][0], grid[i][0], or 0 satisfies the condition.

3. Single-row grid:
    If the grid has only one row, horizontal splitting is not possible, so this case can be skipped.

In all other cases, any element in the upper part of the grid can be considered for deletion.

All scenarios are covered after performing three rotations.

## Complexity Analysis
Let m be the number of rows and n be the number of columns in the grid.

- Time complexity: O(mn).
- Space complexity: O(mn).