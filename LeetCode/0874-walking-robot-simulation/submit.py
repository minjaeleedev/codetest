from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def rot(idx: int, cmd: int) -> str:
            if cmd == -1:
                return (idx + 1) % 4

            return (idx - 1) % 4

        idx = 0
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        res = 0
        obs_x = defaultdict(list)
        obs_y = defaultdict(list)
        for ox, oy in obstacles:
            obs_x[ox].append(oy)
            obs_y[oy].append(ox)

        for k, v in obs_x.items():
            v.sort()
        for k, v in obs_y.items():
            v.sort()

        for cmd in commands:
            if cmd == -1 or cmd == -2:
                idx = rot(idx, cmd)
                continue

            dx, dy = d[idx]
            tx, ty = x + cmd * dx, y + cmd * dy
            rx, ry = x, y
            if dx != 0:
                obs = obs_y[y]
                if not obs:
                    rx = tx
                elif dx < 0:
                    x_index = bisect_left(obs, x)
                    ox = obs[x_index - 1]
                    rx = ox + 1 if tx <= ox < x else tx
                else:
                    x_index = bisect_left(obs, x)
                    if x_index >= len(obs):
                        rx = tx
                    else:
                        ox = obs[x_index]
                        rx = ox - 1 if x < ox <= tx else tx
                x = rx
            else:
                obs = obs_x[x]
                if not obs:
                    ry = ty
                elif dy < 0:
                    y_index = bisect_left(obs, y)
                    oy = obs[y_index - 1]
                    ry = oy + 1 if ty <= oy < y else ty
                else:
                    y_index = bisect_left(obs, y)
                    if y_index >= len(obs):
                        ry = ty
                    else:
                        oy = obs[y_index]
                        ry = oy - 1 if y < oy <= ty else ty
                y = ry

            res = max(res, x**2 + y**2)

        return res
