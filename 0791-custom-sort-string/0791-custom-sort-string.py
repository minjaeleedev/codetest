class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idx = {c:i for i, c in enumerate(order)}
        result = ''.join(sorted(list(s), key=lambda x: idx[x] if x in idx else 27))

        return result