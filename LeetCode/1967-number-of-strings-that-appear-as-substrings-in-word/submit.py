from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum([1 if q in word else 0 for q in patterns])
