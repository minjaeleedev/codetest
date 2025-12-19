from collections import defaultdict, deque

from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        meetings.sort(key=lambda x: (x[2], x[0] != firstPerson, x[1] != firstPerson))
        shared = set([0, firstPerson])
        i = 0
        while i < len(meetings):
            x, y, time = meetings[i]
            j = i
            t = time
            same_times = defaultdict(list)
            while j < len(meetings) and meetings[j][2] == t:
                cx, cy, ct = meetings[j]
                same_times[cx].append(cy)
                same_times[cy].append(cx)
                j += 1

            node = same_times.keys()
            intersection = set(node) & shared
            if intersection:
                # bfs
                visit = {i: False for i in node}
                q = deque(list(intersection))
                for s in intersection:
                    visit[s] = True

                while q:
                    cur = q.popleft()
                    for nxt in same_times[cur]:
                        if not visit[nxt]:
                            visit[nxt] = True
                            q.append(nxt)

                for k, v in visit.items():
                    if v:
                        shared.add(k)

            i = j

        return list(shared)
