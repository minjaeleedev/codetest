class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        return min(map(lambda x: x[0]+x[1], tasks))