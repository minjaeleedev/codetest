## Approach: Dynamic Programming

### Intuition
Let the sum of the elements in array nums be numSum. According to the formula, we can obtain:

- $F(0)=0×nums[0]+1×nums[1]+…+(n−1)×nums[n−1]$
- $F(1)=1×nums[0]+2×nums[1]+…+0×nums[n−1]=F(0)+numSum−n×nums[n−1]$

More generally, when $1≤k<n$, $F(k)=F(k−1)+numSum−n×nums[n−k]$. 
We can iteratively calculate different F(k) values and find the maximum.

### Complexity Analysis
Let n be the length of the array nums.

- Time complexity: O(n).

    Computing numSum takes O(n) time, and computing the initial value F(0) also takes O(n) time since we iterate through the array once. After that, we perform n−1 iterations to compute the remaining values of F(k). Each iteration updates the value using the recurrence relation:

    F(k)=F(k−1)+numSum−n⋅nums[n−k]

    This update only involves a constant number of arithmetic operations, so each iteration takes O(1) time. Therefore, the total time complexity is:

    O(n)+O(n)+O(n)=O(n)

    Overall, the algorithm runs in linear time.

- Space complexity: O(1).

Only a few variables were used.