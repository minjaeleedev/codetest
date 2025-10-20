from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        inc = set(["X++", "++X"])
        dec = set(["X--", "--X"])
        return 0 + sum([1 if op in inc else -1 for op in operations])
