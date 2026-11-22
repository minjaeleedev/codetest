class Solution:
    def checkString(self, s: str) -> bool:
        b = False
        for c in s:
            if c == "b":
                b = True
            else:
                if b:
                    return False

        return True
