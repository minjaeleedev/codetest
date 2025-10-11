class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(1,len(prices)):
            cur, prev = prices[i], prices[i-1]
            if cur - prev > 0:
                result += cur - prev
        
        return result