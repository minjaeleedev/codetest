from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]):
        n = len(strs)
        m = len(strs[0])
        settled = [False] * (n - 1)
        deleted = 0

        for col in range(m):
            # Step 1: Check if keeping this column would break any unsettled pair
            should_delete = False
            for j in range(n - 1):
                if not settled[j] and strs[j][col] > strs[j + 1][col]:
                    should_delete = True
                    break

            if should_delete:
                deleted += 1
            else:
                # Step 2: Update settled status for pairs that become strictly ordered
                for j in range(n - 1):
                    if strs[j][col] < strs[j + 1][col]:
                        settled[j] = True

        return deleted
