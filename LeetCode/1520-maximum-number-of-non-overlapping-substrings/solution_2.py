from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        ls = []
        first = {}
        last = {}
        n = len(s)

        for i in range(n):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        intervals = []

        for i in first:
            start = first[i]
            end = last[i]
            flag = True
            j = start

            while j <= end:
                if first[s[j]] < start:
                    flag = False
                    break

                end = max(end, last[s[j]])
                j += 1

            if flag:
                intervals.append([start, end])

        intervals.sort(key=lambda i: i[1])

        prev = -1

        for i in intervals:
            if i[0] > prev:
                ls.append(s[i[0] : i[1] + 1])
                prev = i[1]

        return ls
