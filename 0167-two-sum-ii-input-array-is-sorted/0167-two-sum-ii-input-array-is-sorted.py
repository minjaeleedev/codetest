class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l, h = 0, len(numbers) - 1
        while l < h:
            s = numbers[l] + numbers[h]
            if s == target:
                res = [l+1, h+1]
                break
            elif s < target:
                l += 1
            else:
                h -= 1
        
        return res