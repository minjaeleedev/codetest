## Overview

## Approach 1: Breadth First Search

### Intuition

### Algorithm

### Implementation

```python
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Queue for BFS. It will store (person, time of knowing the secret)
        q = deque()
        q.append((0, 0))
        q.append((firstPerson, 0))

        # Do BFS
        while q:
            person, time = q.popleft()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    q.append((next_person, t))

        # Since we visited only those people who know the secret,
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]
```

### Complexity Analysis

Let $N$ be the number of people, and $M$ be the number of meetings.

- Time complexity: $O(M \dot (M + N))$

- Space complexity: $O(M + N)$

## Approach 2: Depth First Search

### Intuition

### Algorithm


### Implementation

```python
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Earliest time at which a person learned the secret
        # as per current state of knowledge. If due to some new information,
        # the earliest time of knowing the secret changes, we will update it
        # and again process all the people whom he/she meets after the time
        # at which he/she learned the secret.
        earliest = [inf] * n
        earliest[0] = 0
        earliest[firstPerson] = 0

        # Stack for DFS. It will store (person, time of knowing the secret)
        stack = [(0, 0), (firstPerson, 0)]

        # Do DFS
        while stack:
            person, time = stack.pop()
            for t, next_person in graph[person]:
                if t >= time and earliest[next_person] > t:
                    earliest[next_person] = t
                    stack.append((next_person, t))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if earliest[i] != inf]
```

### Complexity Analysis

## Approach 3: Earliest Informed First Traversal

### Intuition

### Algorithm

### Implementation
```python
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # For every person, store the time and label of the person met.
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((t, y))
            graph[y].append((t, x))

        # Priority Queue for BFS. It stores (time secret learned, person)
        # It pops the person with the minimum time of knowing the secret.
        pq = []
        heappush(pq, (0, 0))
        heappush(pq, (0, firstPerson))

        # Visited array to mark if a person is visited or not.
        # We will mark a person as visited after it is dequeued
        # from the queue.
        visited = [False] * n

        # Do BFS, but pop minimum.
        while pq:
            time, person = heappop(pq)
            if visited[person]:
                continue
            visited[person] = True
            for t, next_person in graph[person]:
                if not visited[next_person] and t >= time:
                    heappush(pq, (t, next_person))

        # Since we visited only those people who know the secret
        # we need to return indices of all visited people.
        return [i for i in range(n) if visited[i]]
```

### Complexity Analysis

## Approach 4: Breadth First Search on Time Scale

### Intuition

### Algorithm

### Implementation

```python
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Sort meetings in increasing order of time
        meetings.sort(key=lambda x: x[2])

        # Group Meetings in increasing order of time
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        # Boolean Array to mark if a person knows the secret or not
        knows_secret = [False] * n
        knows_secret[0] = True
        knows_secret[firstPerson] = True

        # Process in increasing order of time
        for t in same_time_meetings:
            # For each person, save all the people whom he/she meets at time t
            meet = defaultdict(list)
            for x, y in same_time_meetings[t]:
                meet[x].append(y)
                meet[y].append(x)

            # Start traversal from those who already know the secret at time t
            # Set to avoid redundancy
            q = set()
            for x, y in same_time_meetings[t]:
                if knows_secret[x]:
                    q.add(x)
                if knows_secret[y]:
                    q.add(y)

            # Do BFS
            q = deque(q)
            while q:
                person = q.popleft()
                for next_person in meet[person]:
                    if not knows_secret[next_person]:
                        knows_secret[next_person] = True
                        q.append(next_person)

        # List of people who know the secret
        return [i for i in range(n) if knows_secret[i]]
```

### Complexity Analysis

## Approach 5: Union-Find with Reset

### Intuition

### Algorithm

### Implementation

```python
class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Sort meetings in increasing order of time
        meetings.sort(key=lambda x: x[2])

        # Group Meetings in increasing order of time
        same_time_meetings = defaultdict(list)
        for x, y, t in meetings:
            same_time_meetings[t].append((x, y))

        # Create graph
        graph = UnionFind(n)
        graph.unite(firstPerson, 0)

        # Process in increasing order of time
        for t in same_time_meetings:
            # Unite two persons taking part in a meeting
            for x, y in same_time_meetings[t]:
                graph.unite(x, y)

            # If any one knows the secret, both will be connected to 0.
            # If no one knows the secret, then reset.
            for x, y in same_time_meetings[t]:
                if not graph.connected(x, 0):
                    # No need to check for y since x and y were united
                    graph.reset(x)
                    graph.reset(y)

        # Al those who are connected to 0 will know the secret
        return [i for i in range(n) if graph.connected(i, 0)]


class UnionFind:
    def __init__(self, nodes: int):
        # Initialize parent and rank arrays
        self.parent = [i for i in range(nodes)]
        self.rank = [0] * nodes

    def find(self, x: int) -> int:
        # Find the parent of node x. Use Path Compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x: int, y: int) -> None:
        # Unite two nodes x and y, if they are not already united
        px = self.find(x)
        py = self.find(y)
        if px != py:
            # Union by Rank Heuristic
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1

    def connected(self, x: int, y: int) -> bool:
        # Check if two nodes x and y are connected or not
        return self.find(x) == self.find(y)

    def reset(self, x: int) -> None:
        # Reset the initial properties of node x
        self.parent[x] = x
        self.rank[x] = 0
```

### Complexity Analysis