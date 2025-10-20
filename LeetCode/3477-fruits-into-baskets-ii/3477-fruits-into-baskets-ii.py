class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        result = 0
        for i in range(n):
            idx = -1
            for j in range(n):
                if baskets[j] < 0:
                    continue
                if fruits[i] <= baskets[j]:
                    baskets[j] *= -1
                    idx = j
                    break
            
            if idx < 0:
                result += 1
        
        return result