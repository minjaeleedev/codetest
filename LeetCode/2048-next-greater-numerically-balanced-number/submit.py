from collections import Counter


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        end = 1224444

        def is_balanced(num):
            cnt = Counter(str(num))
            for k, v in cnt.items():
                if int(k) != v:
                    return False

            return True

        for i in range(n + 1, end + 1):
            if is_balanced(i):
                return i

        return end
