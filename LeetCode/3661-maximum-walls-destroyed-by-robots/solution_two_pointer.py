from typing import List


class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        robots_to_distance = {}

        for i in range(n):
            robots_to_distance[robots[i]] = distance[i]

        robots.sort()
        walls.sort()

        m = len(walls)
        right_ptr = left_ptr = cur_ptr = robot_ptr = 0

        for i in range(n):
            while right_ptr < m and walls[right_ptr] <= robots[i]:
                right_ptr += 1
            pos1 = right_ptr

            while cur_ptr < m and walls[cur_ptr] < robots[i]:
                cur_ptr += 1
            pos2 = cur_ptr

            if i >= 1:
                left_bound = max(
                    robots[i] - robots_to_distance[robots[i]], robots[i - 1] + 1
                )
            else:
                left_bound = robots[i] - robots_to_distance[robots[i]]

            while left_ptr < m and walls[left_ptr] < left_bound:
                left_ptr += 1
            left_pos = left_ptr
            left[i] = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robots[i] + robots_to_distance[robots[i]], robots[i + 1] - 1
                )
            else:
                right_bound = robots[i] + robots_to_distance[robots[i]]

            while right_ptr < m and walls[right_ptr] <= right_bound:
                right_ptr += 1
            right_pos = right_ptr
            right[i] = right_pos - pos2

            if i == 0:
                continue

            while robot_ptr < m and walls[robot_ptr] < robots[i - 1]:
                robot_ptr += 1
            pos3 = robot_ptr
            num[i] = pos1 - pos3

        sub_left, sub_right = left[0], right[0]
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            sub_left, sub_right = current_left, current_right

        return max(sub_left, sub_right)
