class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i, c in enumerate(s):
            result += (abs(ord('z')-ord(c)) + 1) * (i+1)

        return result