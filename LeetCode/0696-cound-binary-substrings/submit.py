class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        is_zero = s[0] == "0"
        zero, one = 0, 0
        res = 0
        for c in s:
            if c == "0" and is_zero:
                zero += 1
            elif c == "1" and not is_zero:
                one += 1
            elif c == "0" and not is_zero:
                res += min(zero, one)
                zero = 1
                is_zero = True
            else:
                res += min(zero, one)
                one = 1
                is_zero = False

        return res + min(zero, one)
