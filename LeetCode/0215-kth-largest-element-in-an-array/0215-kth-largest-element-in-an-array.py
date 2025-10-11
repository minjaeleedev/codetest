import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)
        for n in nums:
            if len(heap) < k:
                heapq.heappush(heap, n)
            elif len(heap) == k:
                if heap[0] < n:
                    heapq.heappop(heap)
                    heapq.heappush(heap, n)
        
        return heap[0]