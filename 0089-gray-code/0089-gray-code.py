class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        prev = self.grayCode(n-1)
        res = [num | (1 << n-1) if n>1 else 1 for num in reversed(prev)]

        return prev+res

