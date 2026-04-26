## Preface
For a grid grid of size m×n, we can treat each position as a node and connect an undirected edge between any two adjacent nodes (up, down, left, right) that have the same value. In this way, a cycle in grid corresponds to a cycle in the constructed graph. Therefore, the problem reduces to checking whether a cycle exists in this graph.

Common approaches for detecting cycles in an undirected graph include depth-first search (DFS) and breadth-first search (BFS). However, here we introduce an approach based on the Union-Find data structure.

## Approach: Union-Find Set
### Intuition

Using a Union-Find data structure to detect cycles in an undirected graph is both concise and intuitive:

For any edge (x,y) in the graph, we attempt to merge the sets containing x and y. 
If x and y are already in the same set, it means they are already connected, and adding the edge (x,y) will form a cycle.

We can apply this idea by traversing each position in the array grid. 
If the current position has the same value as the position above or to the left, then there exists an edge, and we attempt to merge the corresponding nodes. 
This ensures that each edge is processed only once.

Since the Union-Find structure is one-dimensional while grid is two-dimensional, we map each position (i,j) to a one-dimensional index using i×n+j:

- The position above (i,j) maps to (i−1)×n+j.
- The position to the left of (i,j) maps to i×n+j−1.

### Complexity Analysis

- Time complexity: O(mn⋅α(mn)).

The Union-Find structure uses path compression and union by size or rank, resulting in an amortized cost of α(mn) per operation. Each position participates in at most two union operations, leading to a total complexity of O(mn⋅α(mn)).

- Space complexity: O(mn).

This is the space required for the Union-Find data structure.

