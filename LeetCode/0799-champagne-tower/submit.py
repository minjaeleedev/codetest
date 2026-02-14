class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        for r, arr in enumerate(tower):
            if r == 0:
                arr[0] = poured
                continue

            for g in range(len(arr)):
                left = tower[r - 1][g - 1] if g != 0 else 0
                right = tower[r - 1][g] if g != len(arr) - 1 else 0
                flow_l = (left - 1) / 2 if left > 1 else 0
                flow_r = (right - 1) / 2 if right > 1 else 0
                arr[g] = flow_l + flow_r

        return min(1, tower[query_row][query_glass])
