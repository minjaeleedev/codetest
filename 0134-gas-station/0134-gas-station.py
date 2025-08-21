class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # intuition : wherever you start, gas and cost are equal.
        n = len(gas)
        start = 0
        total, cur = 0, 0
        for i in range(n):
            plus = gas[i] - cost[i]
            total += plus
            cur += plus

            if cur < 0:
                # reset starting point
                cur = 0
                start = i + 1
        
        return -1 if total < 0 else start