class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        result = [cost[0]]
        n = len(cost)
        for i in range(1, n):
            val = min(cost[i], result[-1])
            result.append(val)

        return result 

        