from typing import List


class Solution:
    """
    Approach 2: Preprocessing Nearest Left and Right Positions + Hash Table

    Intuition
    In this approach, we preprocess the nearest positions of elements with the same value on both the left and right sides for every index.
    We store these in two arrays:
    - left[i]: the nearest index to the left of i with the same value
    - right[i]: the nearest index to the right of i with the same value
    To compute these efficiently, we use a hash table to track the most recent occurrence of each value.
    We traverse the array twice:

    First pass (left to right, from −n to n−1): used to fill the left array
    Second pass (right to left, from 2n−1 to 0): used to fill the right array
    The extended traversal handles the cyclic nature of the array.

    For each query index i, we check whether the nearest same-value element is at a distance equal to n.
    If so, it means the element appears only once in the array, so the answer is −1.
    Otherwise, we compute the distances to the nearest matching elements on both sides and take the minimum.
    """

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries
