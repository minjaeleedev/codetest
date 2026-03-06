class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        is_zero = False
        for c in s:
            if is_zero and c == "1":
                return False
            if c == "0":
                is_zero = True

        return True
