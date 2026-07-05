from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        res = [[[0, -1] for _ in range(n)] for _ in range(n)]
        res[n - 1][n - 1] = [0, 1]
        res[0][0] = [0, 0]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == "X" or board[i][j] == "S":
                    continue

                cur_score = int(board[i][j]) if board[i][j] != "E" else 0
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    pr, pc = i + dr, j + dc
                    if not (0 <= pr < n and 0 <= pc < n):
                        continue

                    if res[pr][pc][1] == -1:
                        continue

                    score = res[pr][pc][0] + cur_score
                    if res[i][j][0] < score:
                        res[i][j] = [score, res[pr][pc][1]]
                    elif res[i][j][0] == score:
                        res[i][j][1] = (res[i][j][1] + res[pr][pc][1]) % MOD

        return res[0][0]
