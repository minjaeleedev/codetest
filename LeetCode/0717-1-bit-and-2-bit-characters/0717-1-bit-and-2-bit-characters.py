from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cur = ""
        result = True
        for b in bits:
            cur += str(b)
            if cur == "0":
                result = True
                cur = ""
            elif cur == "10" or cur == "11":
                result = False
                cur = ""

        return result
