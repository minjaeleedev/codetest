class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        # take land first

        n = len(landStartTime)
        minEnd = float('inf')
        for i in range(n):
            minEnd = min(minEnd, landStartTime[i] + landDuration[i])
        m = len(waterStartTime)

        for i in range(m):
            ans = min(ans, waterDuration[i] + max(minEnd, waterStartTime[i]))

        # take water first
        minEnd = float('inf')
        for i in range(m):
            minEnd = min(minEnd, waterStartTime[i] + waterDuration[i])

        for i in range(n):
            ans = min(ans, landDuration[i] + max(minEnd, landStartTime[i]))

        return ans