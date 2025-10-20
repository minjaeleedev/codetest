from collections import Counter
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = Counter()
        for response in responses:
            uniq = set(response)
            for word in uniq:
                cnt[word] += 1

        mx = 0
        result = None
        for k, v in cnt.items():
            if v > mx:
                mx = v
                result = k
            elif v == mx:
                result = min(result, k) if result else k

        return result
