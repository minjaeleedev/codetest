class Solution:
    def longestBalanced(self, s: str) -> int:
        prefix = [[0, 0, 0]]
        for c in s:
            prefix.append(prefix[-1][:])
            prefix[-1]["abc".index(c)] += 1

        ans = 0
        m = {}
        for i, (a, b, c) in enumerate(prefix):
            for k in [
                (-1, a - b, a - c),  # a,b,c
                (-2, a - b, c),  # a,b
                (-3, b - c, a),  # b,c
                (-4, c - a, b),  # a,c
                (-5, b, c),  # a
                (-6, c, a),  # b
                (-7, a, b),  # c
            ]:
                if k not in m:
                    m[k] = i
                else:
                    ans = max(ans, i - m[k])

        return ans
