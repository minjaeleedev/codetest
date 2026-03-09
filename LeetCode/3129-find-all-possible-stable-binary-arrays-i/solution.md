## Approach: Bottom-Up Dynamic Programming with Inclusion-Exclusion

### Intuition

We need to count binary arrays of length $zero + one$ that contain exactly $zero$ 0s and $one$ 1s, where no subarray of length greater than $limit$ consists of the same element.

The key insight is to define a DP state that tracks how many 0s and 1s we've placed so far, and what the last element placed was. This lets us enforce the constraint that no more than $limit$ consecutive identical elements appear.

### DP State Definition

Let $dp[i][j][k]$ be the number of stable binary arrays using exactly $i$ zeros and $j$ ones, where the last element placed is $k$ ($k = 0$ or $k = 1$).

### Base Cases

- $dp[i][0][0] = 1$ for $1 \le i \le \min(zero, limit)$
  - An array of all 0s is valid as long as its length doesn't exceed $limit$.
- $dp[0][j][1] = 1$ for $1 \le j \le \min(one, limit)$
  - An array of all 1s is valid as long as its length doesn't exceed $limit$.

### Transition

To build $dp[i][j][0]$ (placing a 0 at the end):

$$
dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
$$

This means we can extend any array that used $i-1$ zeros and $j$ ones by appending a 0, regardless of whether the previous last element was 0 or 1.

However, if $i > limit$, we are overcounting: arrays where the last $limit + 1$ elements are all 0s are invalid. The number of such invalid arrays equals $dp[i - limit - 1][j][1]$, because the only way to have $limit + 1$ trailing zeros is if the element before those zeros was a 1.

Thus, when $i > limit$:

$$
dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1] - dp[i - limit - 1][j][1]
$$

By symmetry, for $dp[i][j][1]$ (placing a 1 at the end):

$$
dp[i][j][1] = dp[i][j-1][1] + dp[i][j-1][0]
$$

And when $j > limit$:

$$
dp[i][j][1] = dp[i][j-1][1] + dp[i][j-1][0] - dp[i][j - limit - 1][0]
$$

### Why the Subtraction Works (Inclusion-Exclusion)

Consider computing $dp[i][j][0]$. The term $dp[i-1][j][0] + dp[i-1][j][1]$ counts all arrays ending in 0 with $i$ zeros and $j$ ones, but some may have more than $limit$ consecutive 0s at the end.

If there are $limit + 1$ or more consecutive 0s at the end, then removing the last $limit + 1$ zeros gives an array with $i - limit - 1$ zeros and $j$ ones that must end in 1 (otherwise we'd have even more consecutive 0s). This count is exactly $dp[i - limit - 1][j][1]$.

### Final Answer

$$
\text{answer} = (dp[zero][one][0] + dp[zero][one][1]) \mod (10^9 + 7)
$$

### Implementation

```python
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0, 0] for _ in range(one + 1)] for _ in range(zero + 1)]
        mod = int(1e9 + 7)
        for i in range(min(zero, limit) + 1):
            dp[i][0][0] = 1
        for j in range(min(one, limit) + 1):
            dp[0][j][1] = 1
        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                if i > limit:
                    dp[i][j][0] = (
                        dp[i - 1][j][0] + dp[i - 1][j][1] - dp[i - limit - 1][j][1]
                    )
                else:
                    dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1]
                dp[i][j][0] = (dp[i][j][0] % mod + mod) % mod
                if j > limit:
                    dp[i][j][1] = (
                        dp[i][j - 1][1] + dp[i][j - 1][0] - dp[i][j - limit - 1][0]
                    )
                else:
                    dp[i][j][1] = dp[i][j - 1][1] + dp[i][j - 1][0]
                dp[i][j][1] = (dp[i][j][1] % mod + mod) % mod
        return (dp[zero][one][0] + dp[zero][one][1]) % mod
```

### Complexity Analysis

Let $Z$ = `zero`, $O$ = `one`, and $L$ = `limit`.

- **Time complexity:** $O(Z \cdot O)$

  We iterate over all $(i, j)$ pairs where $1 \le i \le Z$ and $1 \le j \le O$. Each cell is computed in $O(1)$ time using previously computed values.

- **Space complexity:** $O(Z \cdot O)$

  The 3D DP table has dimensions $(Z+1) \times (O+1) \times 2$, which simplifies to $O(Z \cdot O)$.
