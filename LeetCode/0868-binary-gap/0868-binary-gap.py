class Solution:
    def binaryGap(self, n: int) -> int:
        b = str(bin(n))[2:]
        left = -1
        result = 0
        for r in range(len(b)):
            ch = b[r]
            if ch == "1":
                if left != -1:
                    result = max(result, r - left)
                left = r

        return result
