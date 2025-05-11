class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        mosts = []
        heapq.heapify(mosts)
        for key,val in cnt.items():
            if len(mosts) < k:
                heapq.heappush(mosts, (val,key))
                continue

            freq, num = heapq.heappop(mosts)
            if freq < val:
                heapq.heappush(mosts, (val,key))
            else:
                heapq.heappush(mosts, (freq,num))
        
        return [num for _,num in mosts]