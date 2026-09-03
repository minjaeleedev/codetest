class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        tmp = 1 if nums1[0] % 2 else 2
        mn = nums1[0]
        for n in nums1[1:]:
            tmp &= 1 if n % 2 else 2
            mn = min(n, mn)

        if tmp:
            return True

        return (mn % 2) == 1
