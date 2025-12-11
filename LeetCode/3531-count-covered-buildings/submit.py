from collections import defaultdict
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_dict = defaultdict(list)
        y_dict = defaultdict(list)
        for x, y in buildings:
            x_dict[x].append(y)
            y_dict[y].append(x)

        for _, xls in x_dict.items():
            xls.sort()

        for _, yls in y_dict.items():
            yls.sort()

        res = 0
        for cx, cy in buildings:
            y_list = x_dict[cx]
            if len(y_list) <= 2:
                continue

            if y_list[0] == cy or y_list[-1] == cy:
                continue

            x_list = y_dict[cy]
            if len(x_list) <= 2:
                continue

            if x_list[0] == cx or x_list[-1] == cx:
                continue

            res += 1

        return res
