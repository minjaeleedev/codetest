# Approach: Square Root Decomposition + Difference Array

## Intuition
The most straightforward approach is to simulate each query directly by multiplying elements one by one. 
The time complexity for a single query is $$O(n)$$, and for q queries, it becomes O(nq), which is around 10<sup>10</sup> and will lead to a timeout.
The main issue is that when k is small, a single query accesses many elements, making it expensive.

We observe that the step size k affects the complexity differently, so we divide the queries into two categories based on the relationship between k and n, and handle each category separately:

- When k≥n, each query touches at most $ {k \over n} <= \sqrt n $
  elements, so a brute force approach is acceptable. The total time complexity in this case is $ O(q \sqrt n) $

- When $k < n$, a single query may access many elements, making the brute force approach inefficient. 

For smaller step sizes ($k<n$), we group queries by their k value so that queries with the same k can be processed together. 
The key observation is that indices affected by the same k form a fixed pattern. 
For example, when k=3, the affected indices are $l,l+3,l+6,…$.

Once k is fixed, each query [l,r,v] multiplies elements at positions l,l+k,l+2k,… by v. 
This is equivalent to performing range multiplication on a subsequence defined by step size k.

To handle this efficiently, we use a difference array dif initialized with all values set to 1. 
For a query [l,r,v], we determine the last affected index and denote the next position as R. 
For example, in the query [2,7,3], the last affected index is 5, so R=8. We then apply:

- $dif[l]=dif[l]×v$
- $dif[R]=dif[R]×v^{−1}$
 
Here, $v^{−1}$ is the modular inverse of v under modulo M=10^9+7, which can be computed using Fermat's Little Theorem as $v^{M−2}$. 

Each query is processed in O(logM) time.

After processing all queries for a fixed k, we traverse the difference array and compute prefix products:

$dif[i]=dif[i]×dif[i−k]$.

This gives the cumulative multiplier for each position. We then apply these values back to the original array in O(n) time.

The total time complexity for handling queries with small step sizes is $O(n\sqrt n+q\log M)$.

Finally, we need to compute R. 
The last affected index is:
$l+\lfloor {{r−l} \over {k}} \rfloor k $

So,

$R=l+(\lfloor {{r-l} \over {k}} \rfloor +1)⋅k$

The maximum possible value of R is n+k. 
For convenience, we use a difference array of size n+T.

## Complexity Analysis
- Time complexity: $O((n+q)\sqrt n+q\log M)$.

- Space complexity: $O(\sqrt n+q)$
