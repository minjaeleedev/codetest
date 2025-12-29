from functools import lru_cache
from collections import defaultdict

from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        blocks = defaultdict(set)
        for s in allowed:
            blocks[s[:2]].add(s[-1])

        @lru_cache
        def helper(path, bottom):
            if len(bottom) == 1:
                return True

            if len(path) == len(bottom) - 1:
                return helper("", path)

            res = False
            sub = bottom[len(path)] + bottom[len(path) + 1]
            if sub not in blocks:
                return False

            for c in blocks[sub]:
                res = res or helper(path + c, bottom)
            return res

        return helper("", bottom)
