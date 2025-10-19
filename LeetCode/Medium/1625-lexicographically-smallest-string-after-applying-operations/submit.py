from collections import deque


# use bfs
# Runtime 4593ms (5.04%)
# Memory 19.39MB (74.82%)
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        prev = set()
        q = deque([s])
        prev.add(s)
        while q:
            cur = q.popleft()
            rot = cur[n - b :] + cur[: n - b]
            arr = list(rot)
            for d in range(10):
                added = d * a
                for i in range(1, n, 2):
                    new_c = (added + int(arr[i])) % 10
                    arr[i] = str(new_c)

                joined = "".join(arr)
                if joined not in prev:
                    prev.add(joined)
                    q.append(joined)

        return min(prev)
