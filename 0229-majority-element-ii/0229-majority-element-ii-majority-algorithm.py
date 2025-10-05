class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # one, two will be majority candidates
        one, two = 0, 0
        one_count, two_count = 0, 0 
        for num in nums:
            if one_count == 0 and num != two:
                one = num
                one_count = 1
                continue
            
            if two_count == 0 and num != one:
                two = num
                two_count = 1
                continue
            
            if num == one:
                one_count += 1
            elif num == two:
                two_count += 1
            else:
                # if different from both, decrement all.
                one_count -= 1
                two_count -= 1

        res = []        

        # count real frequency. 
        one_count = two_count = 0
        for num in nums:
            if num == one:
                one_count += 1
            elif num == two:
                two_count += 1
        
        if one_count > len(nums) // 3:
            res.append(one)
        if two_count > len(nums) // 3:
            res.append(two)

        return res


