from bisect import bisect_left
from typing import List


class Solution:
    """
    Approach: Inclusion-Exclusion Principle + Prefix Sum + Binary Search

    Let n be the length of the array nums, and let m be the maximum value in nums.
    A brute-force approach would enumerate all O(n^2) pairs
    and compute the greatest common divisor (GCD) of each pair.
    Since n can be as large as 10^5, this approach is clearly infeasible.

    The key observation is that although there are many pairs,
    the range of possible GCD values is small.
    every GCD lies in the range [1,m], where m≤5×10^4.
    Therefore, instead of enumerating pairs, we enumerate all possible GCD values
    and count how many pairs have each value as their GCD.

    First, count the occurrences of each value in nums and store them in the array cnt.
    Then, for every positive integer i∈[1,m],
    enumerate all of its multiples to count how many elements in nums are divisible by i.
    Any pair formed from these elements has a GCD of at least i.

    However, "at least i" is not the same as "exactly i",
    because it also includes pairs whose GCD is 2i, 3i, and so on.
    To obtain the number of pairs whose GCD is exactly i,
    we traverse i from large to small and apply the inclusion-exclusion principle.
    Specifically, we first count all pairs whose GCD is at least i,
    then subtract the numbers of pairs whose GCD is 2i, 3i, and so on.
    The remaining count is exactly the number of pairs whose GCD equals i.

    Finally, compute the prefix sum of these counts.
    The prefix sum at index i represents the number of pairs whose GCD is at most i.
    For each query queries[i], we perform a binary search on the prefix sum array
    to find the smallest GCD value whose cumulative count exceeds the query.

    Complexity Analysis

    Let m be the maximum value in nums, and let q be the length of queries.

    - Time complexity: O(mlogm+qlogm).

    Enumerating multiples has harmonic-series complexity of O(mlogm),
    and each binary search takes O(logm) time.

    - Space complexity: O(m).

    An array of size m+1 is required to store the counts.
    """

    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        cnt = [0] * (m + 1)
        for num in nums:
            cnt[num] += 1
        for i in range(1, m + 1):
            for j in range(i * 2, m + 1, i):
                cnt[i] += cnt[j]
        for i in range(1, m + 1):
            cnt[i] = cnt[i] * (cnt[i] - 1) // 2
        for i in range(m, 0, -1):
            for j in range(i * 2, m + 1, i):
                cnt[i] -= cnt[j]
        for i in range(1, m + 1):
            cnt[i] += cnt[i - 1]
        ans = []
        for q in queries:
            q += 1
            pos = bisect_left(cnt, q)
            ans.append(pos)
        return ans
