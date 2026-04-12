# Approach 1: Dynamic Programming
## Intuition
We define dp[i][l][r] as the minimum movement distance required to reach a state where, after typing the i-th character of the string word, the left hand is at position l and the right hand is at position r. Here, the position refers to the index of the character, for example, A corresponds to 0, B corresponds to 1, and so on. This representation maps characters to integers instead of using 2D keyboard coordinates, which simplifies state transitions.

Now, how do we perform the state transitions?

We first observe an important property: for any state dp[i][l][r], either word[i] == l or word[i] == r. In other words, after typing the i-th character, at least one of the hands must be at the position of word[i].

We consider the transitions based on these two cases:

When word[i] == l, the left hand is at the position of word[i]. We consider where the i - 1-th character was typed:

If the left hand was at word[i - 1], then it moves from word[i - 1] to word[i]:

## Complexity Analysis
Let N be the length of the string word, and ∣Σ∣=26.

- Time complexity: O(∣Σ∣N)

For each index i, we iterate over all possible positions. Each transition takes constant time or iterates over ∣Σ∣, leading to an overall complexity of O(∣Σ∣N).

- Space complexity: O(∣Σ∣^2N)

# Approach 2: Dynamic Programming + Space Optimization
## Intuition
From Approach 1, recall the key property: for any state dp[i][l][r], either word[i] == l or word[i] == r. This means that for each i, we only need to store 2∣Σ∣ states instead of ∣Σ∣^2.

We can redefine the state as dp[i][op][rest], where:

op = 0 means the left hand is at word[i]
op = 1 means the right hand is at word[i]
rest represents the position of the other hand
We can simplify this further by observing symmetry. Swapping the roles of the left and right hands does not change the total movement cost. Therefore, dp[i][op = 0][rest] and dp[i][op = 1][rest] are always equal.

This allows us to reduce the state to dp[i][rest], which represents the minimum movement cost when one hand is at word[i] and the other is at position rest. We no longer need to distinguish between left and right hands.

## Complexity Analysis
- Time complexity: O(∣Σ∣N).
- Space complexity: O(∣Σ∣N).