from collections import Counter
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(s1, s2):
            cnt = Counter(s1)
            cnt2 = Counter(s2)
            if len(cnt) != len(cnt2):
                return False

            for k, v in cnt.items():
                if k not in cnt2 or cnt2[k] != v:
                    return False

            return True

        res = [words[0]]
        for i in range(1, len(words)):
            if is_anagram(res[-1], words[i]):
                continue
            else:
                res.append(words[i])

        return res
