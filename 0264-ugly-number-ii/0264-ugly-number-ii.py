class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = []
        nums = set()
        heapq.heappush(heap, 1)
        nums.add(1)
        
        cur = 1
        for _ in range(n):
            cur = heapq.heappop(heap)

            for p in [2,3,5]:
                nxt = cur * p
                if nxt not in nums:
                    heapq.heappush(heap, nxt)
                    nums.add(nxt)
        
        return cur
