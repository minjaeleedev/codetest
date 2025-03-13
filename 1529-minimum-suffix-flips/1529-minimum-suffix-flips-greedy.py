class Solution:
    def minFlips(self, target: str) -> int:
        cur = '0'
        result = 0
        for c in target:
            if c == cur:
                continue
            
            cur = '0' if cur == '1' else '1'
            result += 1

        return result
            