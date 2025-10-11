class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, subset):
            result.append(subset[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1, subset)
                subset.pop()

        result = []
        nums.sort()
        backtrack(0, [])
        return result